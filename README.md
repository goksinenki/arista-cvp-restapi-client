# arista-cvp-restapi-client
Arista CloudVision Portal Rest Api Python Script - Endpoint Search

That's a small python script example which makes the following operations

- read mac addresses from a text file and convert to colon format (mac_unix_expanded)
- connect to Arista Cloud Vision Portal with Rest Api and make a endpoint search with mac addresses
- get the information (switch device id, switch interface, vlan id..etc ) also make a second query and get the switch hostname
- parse the json format and get the required variables
- write the results to another text file in csv format (macadres,switchhostname,deviceid,interface,vlanid)

Installation / Requirements

pip install netaddr
pip install json

You need to generate a token.tok file for authentication (for more info https://www.arista.com/en/cg-cv/cv-service-accounts)

You can develop the script easily for your required job with the help of other functions at https://github.com/aristanetworks/cloudvision-apis/blob/trunk/docs/content/examples/REST/_index.files/examples_python_rest.py

Thank you Arista.

![image](https://user-images.githubusercontent.com/917944/231074679-a9adabad-2b66-4538-a8b1-8647a5fbab60.png)
