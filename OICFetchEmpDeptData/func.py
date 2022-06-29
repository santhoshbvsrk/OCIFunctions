import io
import json
import logging
from fdk import response
import InvokeFetchEmpDeptData as intempdeptdata

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

def handler(ctx, data: io.BytesIO=None):
    idvar=''
    deptvar=''
    resp = {'status':None, 'description':None, 'output':None}
    try:
        body = json.loads(data.getvalue())
        cfg = ctx.Config()
        idvar = body["EmpId"]
        deptvar = body["DeptNo"]
        oicbaseurl = cfg["oic_base_url"]
        oicusername = cfg["oic_username"]
        oicuserpwd = cfg["oic_userpwd"]
        
        resp = intempdeptdata.call_oic(oicbaseurl, oicusername, oicuserpwd, idvar, deptvar)
    
    except (Exception) as ex:
        logging.getLogger().info('error encountered while invoking FetchEmpDeptData {}'.format(str(ex)))
        resp['status'], resp['description'], resp['output'] = 'ERROR in handler exception', str('ex'), 'Errored Out'
    else:
        logging.getLogger().info('No Errors encountered in the handler')

    return response.Response(ctx,response_data=json.dumps(resp),headers={"Content-Type":"application/json"})