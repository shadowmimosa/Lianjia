# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import elasticsearch
import pymongo
import pymysql


class ErshoufangEsPipeline(object):
    def __init__(self, es_index):
        self.es = elasticsearch.Elasticsearch()
        self.es_index = es_index
        self.es_id = 1

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            es_index=crawler.settings.get('ERSHOUFANG')
        )

    def open_spider(self, spider):
        try:
            result = self.es.indices.create(index=self.es_index, ignore=400)
            print(result)
        except Exception:
            pass

    def process_item(self, item, spider):
        result = self.es.create(index=self.es_index, doc_type='ershoufang', id=self.es_id, body=dict(item))
        self.es_id += 1
        print(result)
        return item


class ErshoufangMongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('ERSHOUFANG')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        print(self.db)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        result = self.db[item['city']].insert_one(dict(item))
        print(result)
        return item


class ErshoufangMysql(object):
    def __init__(self, mysql_uri, mysql_db):
        self.mysql_uri = mysql_uri
        self.mysql_db = mysql_db
        self.create_table_sql = """
CREATE TABLE `ershoufang` (
`id` INT ( 11 ) NOT NULL AUTO_INCREMENT,
`city` VARCHAR ( 255 )  NOT NULL DEFAULT '' COMMENT '城市',
`house_url` LONGTEXT  NOT NULL  COMMENT '房产url',
`img_url` LONGTEXT  NOT NULL COMMENT '图片链接',
`title` VARCHAR ( 255 )  NOT NULL DEFAULT '' COMMENT '标题',
`xiaoqu_url` text ( 255 )  NOT NULL COMMENT '小区url',
`xiaoqu_name` VARCHAR ( 255 )  NOT NULL DEFAULT '' COMMENT '小区名',
`huxing` VARCHAR ( 255 )  NOT NULL DEFAULT '' COMMENT '户型',
`position_info` VARCHAR ( 255 )  NOT NULL DEFAULT '' COMMENT '位置信息',
`position` VARCHAR ( 255 )  NOT NULL DEFAULT '' COMMENT '位置',
`position_url` VARCHAR ( 255 )  NOT NULL DEFAULT '' COMMENT '位置url',
`total_price` INT ( 11 )  NOT NULL DEFAULT 0 COMMENT '总价',
`square_price` INT ( 11 )  NOT NULL DEFAULT 0 COMMENT '每平米价格',
`crawl_time` BIGINT  NOT NULL DEFAULT 0,
PRIMARY KEY ( `id` ) 
) ENGINE = INNODB AUTO_INCREMENT = 2 DEFAULT CHARSET = utf8 ;
"""
        self.connection = pymysql.connect(host='39.106.114.90',
                                     user='root',
                                     password='root',
                                     db='lianjia',
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connection.cursor()
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mysql_uri=crawler.settings.get('MYSQL_URI'),
            mysql_db=crawler.settings.get('ERSHOUFANG')
        )

    def open_spider(self, spider):
        try:
            result = self.cursor.execute(self.create_table_sql)
        except:
            pass


    def close_spider(self, spider):
        self.cursor.close()

    def process_item(self, item, spider):
        result = self.db[item['city']].insert_one(dict(item))
        print(result)
        return item
