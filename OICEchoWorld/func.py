import io
import json
import logging
from fdk import response
import InvokeEchoWorld as intechowrld

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

def handler(ctx, data: io.BytesIO=None):
    resp = {'status':None, 'description':None, 'output':None}
    try:
        cfg = ctx.Config()
        oicbaseurl = cfg["oic_base_url"]
        oicusername = cfg["oic_username"]
        oicuserpwd = cfg["oic_userpwd"]
        resp = intechowrld.call_oic(oicbaseurl, oicusername, oicuserpwd)
    
    except (Exception) as ex:
        logging.getLogger().info('error encountered while invoking EchoWorld {}'.format(str(ex)))
        resp['status'], resp['description'], resp['output'] = 'ERROR in handler exception', str('ex'), 'Errored Out'
    else:
        logging.getLogger().info('No Errors encountered in the handler')

    return response.Response(ctx,response_data=json.dumps(resp),headers={"Content-Type":"application/json"})