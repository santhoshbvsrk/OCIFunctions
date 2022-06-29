import logging
import requests
import json
import os
import oci
import base64

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

def call_oic(oicbaseurl, oicusername, oicuserpwd, empid):
    response = {'status':None, 'description':None, 'output':None}
    
    try:
        auth = (oicusername,oicuserpwd)
        resp= requests.get(oicbaseurl,params={"EmpId":empid},headers={'type': 'application/json'},auth=auth)

        logging.getLogger().info('INFO: Calling FetchEmpData Integration is Successful: {0}'.format(str(resp.status_code)))
        
        if resp.status_code==200:
            response["status"], response["description"], response["output"] = "SUCCESS", "Call to OIC is Successful", resp.json()
        else:
            response["status"], response["description"], response["output"] = "ERROR in Int Else", str(resp.status_code), "Errored Out"
    except Exception as ex:
        response["status"], response["description"], response["output"] = "ERROR in Int exception", str(ex), "Errored Out"

    return response