#导入BosClient配置文件
import bos_sample_conf,os,sys
            
#导入BOS相关模块
from baidubce import exception
from baidubce.services import bos
from baidubce.services.bos import canned_acl
from baidubce.services.bos.bos_client import BosClient
from baidubce.services.bos import storage_class
    
#新建BosClient
bos_client = BosClient(bos_sample_conf.config)
#此处输入你的BOS Bucket的名字。
bucket_name = '[BOS Bucket Name]'

response = bos_client.list_objects(bucket_name)
for a in os.walk(sys.path[0]):
    for b in a[2]:
        if b[-4:]=='.mp4':
            print('“%s”开始上传。'%(pa:='%s/%s'%(a[0],b)))
            object_key=b
            bos_client.put_object_from_file(bucket_name,object_key,pa,storage_class=storage_class.STANDARD_IA)
            print('“%s”上传完成。'%pa)
