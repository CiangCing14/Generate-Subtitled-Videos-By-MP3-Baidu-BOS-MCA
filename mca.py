#导入Python标准日志模块
import logging

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
#导入BosClient配置文件
import bos_sample_conf 
            
#导入BOS相关模块
from baidubce import exception
from baidubce.services import bos
from baidubce.services.bos import canned_acl
from baidubce.services.bos.bos_client import BosClient
    
#新建BosClient
bos_client = BosClient(bos_sample_conf.config)

#此处输入你的BOS Bucket Name。
response = bos_client.list_objects(bn:='[BOS Bucket Name]')
sl=[]
for object in response.contents:
    source = "bos://%s/%s"%(bn,object.key)
    print('“%s”开始分析。'%source)
    preset = "run"
    response = vca_client.put_media(source, preset);
    print('“%s”分析请求完毕。'%source)
    sl.append(source)
f=open('sl.txt','w+');f.write(repr(sl));f.close()
