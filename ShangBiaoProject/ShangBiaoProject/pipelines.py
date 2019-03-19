# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#import pymongo
from scrapy.exceptions import DropItem


class ShangbiaoprojectPipeline(object):

    def __init__(self):
        self.ids_seen = set()


    def do_insert(self, item):
        pass


    def process_item(self, item, spider):

        print(item['images'])
        # if item['id'] in self.ids_seen:
        #     raise DropItem('Duplicate item found: %s' % item)
        # else:
        #     self.ids_seen.add(item['id'])
        #     return item
        return item

    def close_spider(self, spider):
        pass



class PicPipeline(object):

    def __init__(self):
        self.ids_seen = set()


    def do_insert(self, item):
        pass


    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem('Duplicate item found: %s' % item)
        else:
            self.ids_seen.add(item['id'])
            return item

    def close_spider(self, spider):
        pass