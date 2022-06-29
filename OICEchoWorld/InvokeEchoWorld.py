import logging
import requests
import json
import os
import oci

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

def call_oic(oicbaseurl, oicusername, oicuserpwd):
    response = {'status':None, 'description':None, 'output':None}
    try:
        auth = (oicusername,oicuserpwd)
        resp= requests.get(oicbaseurl,auth=auth)
        logging.getLogger().info('INFO: Calling EchoWorld Integration is Successful: {0}'.format(str(resp.status_code)))
        if resp.status_code==200:
            response["status"], response["description"], response["output"] = "SUCCESS", "Call to OIC is Successful", resp.json()
        else:
            response["status"], response["description"], response["output"] = "ERROR in Int Else", str(resp.status_code), "Errored Out"
    except Exception as ex:
        response["status"], response["description"], response["output"] = "ERROR in Int exception", str(ex), "Errored Out"

    return response