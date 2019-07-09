# -*- coding: utf-8 -*-

import os


class Doutudemo1Pipeline(object):
    def process_item(self, item, spider):
        path = item['img_name']
        body = item['img']
        if not os.path.exists("imgs"):
            os.mkdir("imgs")
        with open('imgs/{}.jpg'.format(path), 'wb') as f:
            f.write(body)
