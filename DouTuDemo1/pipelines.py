# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Doutudemo1Pipeline(object):
    def process_item(self, item, spider):
        path = item['img_name']
        body = item['img']
        with open('imgs/{}.jpg'.format(path), 'wb') as f:
            f.write(body)
