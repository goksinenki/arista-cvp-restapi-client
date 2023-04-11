#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the COPYING file.

import json
import requests
from json import JSONDecoder, JSONDecodeError
import ssl
import netaddr
from netaddr import *


ssl._create_default_https_context = ssl._create_unverified_context
from pprint import pprint as pp

with open("token.tok") as f:
    token = f.read().strip('\n')

cvp_url = "https://YourCVPIPAddress"
#mac = "0050.56a1.89c7"
#mac = EUI(mac)
#mac.dialect = mac_unix_expanded
#print(mac)
#deviceid = "SGD21019975"

def json_decoder(data):
    decoder = JSONDecoder()
    pos = 0
    result = []
    while True:
        try:
            o, pos = decoder.raw_decode(data, pos)
            result.append(o)
            pos +=1
        except JSONDecodeError:
            break
    return result

def get_deviceinfo():
    event_url = '/api/resources/inventory/v1/Device?key.deviceId=%s'%(deviceid)
    url = cvp_url + event_url
    head = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.get(url, headers=head, verify=False)
    #print(response.text)
    tasks_json = response.json()
    global devicehostname
    devicehostname = (tasks_json["value"]["hostname"])
    #print (devicehostname)

def get_port():
    event_url = '/api/resources/endpointlocation/v1/EndpointLocation?key.searchTerm=%s'%(mac)
    url = cvp_url + event_url
    head = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.get(url, headers=head, verify=False)
    #print(response.text)
    tasks_json = response.json()
    #print (tasks_json["value"]["key"]["searchTerm"])
    global deviceid
    global swport
    uzunluk = len(tasks_json["value"]["deviceMap"])
    print (uzunluk)
    if uzunluk != 0:
        deviceid = (tasks_json["value"]["deviceMap"]["values"]["ENDPOINT_%s"%(mac)]["locationList"]["values"][0]["deviceId"])
        swport = (tasks_json["value"]["deviceMap"]["values"]["ENDPOINT_%s"%(mac)]["locationList"]["values"][0]["interface"])
        vlanid = (tasks_json["value"]["deviceMap"]["values"]["ENDPOINT_%s"%(mac)]["locationList"]["values"][0]["vlanId"])
        get_deviceinfo()
        #print(str(mac) + "," + devicehostname + "," + deviceid + "," + swport + "," + str(vlanid))
        file.write('%s,%s,%s,%s,%s\n'%(mac,devicehostname,deviceid,swport,vlanid))
    else:
        file.write('%s + " not found"\n'%(mac))

file = open('results.txt', 'w')
my_file = open("macadresses.txt", "rb")

try:
    for line in my_file:
            l = [i.strip() for i in line.decode().split(' ')]
            mac = l[0]
            mac = EUI(mac)
            mac.dialect = mac_unix_expanded
            get_port()
    my_file.close()
    file.close()
except Exception:
    pass
