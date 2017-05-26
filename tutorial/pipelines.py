# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


# class SingerPipeline(object):
#     def __init__(self):
#         self.ids_seen = set()
#         self.file = open('items.json', 'wb')
#
#     def close_spider(self, spider):
#         self.file.close()
#
#     def process_item(self, item, spider):
#         print("SingerPipeline:")
#         if item['song_name'] in self.ids_seen:
#             raise DropItem("Duplicate item found: %s" % item)
#         else:
#             self.ids_seen.add(item['song_name'])
#             line = json.dumps(dict(item)) + "\n"
#             print(line)
#             self.file.write(line)
#             return item
