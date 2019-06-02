import time
import os
import elasticsearch
from config import *
es = elasticsearch.Elasticsearch()
if es.indices.exists(ershoufangdb()):
    es.indices.delete(ershoufangdb())