import logging
import requests
import json
import os
import oci
import base64

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

def call_oic(oicbaseurl, oicusername, oicuserpwd, name):
    response = {'status':None, 'description':None, 'output':None}
    
    try:
        auth = (oicusername,oicuserpwd)
        resp= requests.get(oicbaseurl,params={"Name":name},headers={'type': 'application/json'},auth=auth)
        logging.getLogger().info('INFO: Calling HelloWorld Integration is Successful: {0}'.format(str(resp.status_code)))
        if resp.status_code==200:
            response["status"], response["output"] = "SUCCESS", resp.json()["Message"]
        else:
            response["status"], response["description"] = "ERROR in Int Else", str(resp.status_code)
    except Exception as ex:
        response["status"], response["description"] = "ERROR in Int exception", str(ex)

    return response