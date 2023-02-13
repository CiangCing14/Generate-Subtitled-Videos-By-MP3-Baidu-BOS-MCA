#导入BosClient配置文件
import bos_sample_conf 
            
#导入BOS相关模块
from baidubce import exception
from baidubce.services import bos
from baidubce.services.bos import canned_acl
from baidubce.services.bos.bos_client import BosClient
    
#新建BosClient
bos_client = BosClient(bos_sample_conf.config)
bucket_name = '[BOS Bucket Name]'

response = bos_client.list_objects(bucket_name)
for object in response.contents:
    try:
        response = bos_client.get_object_meta_data(bucket_name, object.key)
        bos_client.delete_object(bucket_name, object.key)
        print('已删除',object.key)
    except exception.BceError as e:
        print('已不存在',object.key)
