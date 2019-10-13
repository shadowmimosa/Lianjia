import pymongo
import time
from config.configs import *
client = pymongo.MongoClient(host='39.106.114.90')
db = 'lianjia_ershoufang' + str(time.strftime('%Y%m%d', time.localtime(time.time())))
db = client[db]
collections = db.list_collection_names()
print(collections)