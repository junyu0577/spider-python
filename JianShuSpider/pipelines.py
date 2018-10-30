# -*- coding: utf-8 -*-
import  pymongo
from JianShuSpider.settings import mongo_host,mongo_port,mongo_db_name,mongo_db_collection
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JianshuspiderPipeline(object):

    def __init__(self):
        host = mongo_host
        port = mongo_port
        db_name = mongo_db_name
        post = mongo_db_collection

        client = pymongo.MongoClient(host=host,port = port)
        mydb = client[db_name]
        self.post = mydb[post]
        #去重 先删除表中所有记录
        self.post.remove({})

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
