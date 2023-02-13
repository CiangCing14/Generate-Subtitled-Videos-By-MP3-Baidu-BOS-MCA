#导入Python标准日志模块
import logging,time

#从Python SDK导入MCA配置管理模块以及安全认证模块  
from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.auth.bce_credentials import BceCredentials

#设置VcaClient的Host，Access Key ID和Secret Access Key
vca_host = "vca.bj.baidubce.com"
access_key_id = "[AK]"
secret_access_key = "[SK]"

#设置日志文件的句柄和日志级别
logger = logging.getLogger('baidubce.http.bce_http_client')
fh = logging.FileHandler("sample.log")
fh.setLevel(logging.DEBUG)

#设置日志文件输出的顺序、结构和内容
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)

#创建BceClientConfiguration
config = BceClientConfiguration(credentials=BceCredentials(access_key_id, secret_access_key), endpoint = 'vca.bj.baidubce.com')

#导入MCA相关模块
from baidubce import exception
from baidubce.services import vca
from baidubce.services.vca.vca_client import VcaClient

#新建VcaClient
vca_client = VcaClient(config)

f=open('sl.txt','r');sl=eval(f.read());f.close()
for a in sl:
    source = a
    n=0
    while True:
        response = vca_client.get_media(source).status
        print('“%s”状态为“%s”，已用%ds…'%(source,response,n))
        if response=='FINISHED':break
        time.sleep(1)
        n+=1
    subtask_type = 'speech'
    response = vca_client.get_sub_task(source,subtask_type)
    f=open('%s.json'%'.'.join(a.split('/')[-1].split('.')[:-1]),'w+');f.write(str(response.result));f.close()
    print('“%s”结果下载完毕。'%source)
