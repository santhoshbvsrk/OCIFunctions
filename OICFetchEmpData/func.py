import io
import json
import logging
from fdk import response
import InvokeFetchEmpData as intfetchempdata

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

def handler(ctx, data: io.BytesIO=None):
    idvar=''
    resp = {'status':None, 'description':None, 'output':None}
    try:
        body = json.loads(data.getvalue())
        cfg = ctx.Config()
        idvar = body["EmpId"]
        oicbaseurl = cfg["oic_base_url"]
        oicusername = cfg["oic_username"]
        oicuserpwd = cfg["oic_userpwd"]
        
        resp = intfetchempdata.call_oic(oicbaseurl, oicusername, oicuserpwd, idvar)
    
    except (Exception) as ex:
        logging.getLogger().info('error encountered while invoking FetchEmpData {}'.format(str(ex)))
        resp['status'], resp['description'], resp['output'] = 'ERROR in handler exception', str('ex'), 'Errored Out'
    else:
        logging.getLogger().info('No Errors encountered in the handler')

    return response.Response(ctx,response_data=json.dumps(resp),headers={"Content-Type":"application/json"})