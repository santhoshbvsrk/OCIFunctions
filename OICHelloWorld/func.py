import io
import json
import logging
from fdk import response
import InvokeHelloWorld as inthellowrld

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

def handler(ctx, data: io.BytesIO=None):
    namevar=''
    resp = {'status':None, 'description':None, 'output':None}
    try:
        body = json.loads(data.getvalue())
        cfg = ctx.Config()
        namevar = body["Name"]
        oicbaseurl = cfg["oic_base_url"]
        oicusername = cfg["oic_username"]
        oicuserpwd = cfg["oic_userpwd"]
        
        resp = inthellowrld.call_oic(oicbaseurl, oicusername, oicuserpwd, namevar)
    
    except (Exception) as ex:
        logging.getLogger().info('error encountered while invoking hello world {}'.format(str(ex)))
        resp['status'],resp['description']='ERROR in handler exception',str('ex')
    else:
        logging.getLogger().info('No Errors encountered in the handler')

    return response.Response(ctx,response_data=json.dumps(resp),headers={"Content-Type":"application/json"})