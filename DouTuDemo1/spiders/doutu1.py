# -*- coding: utf-8 -*-
import scrapy
import re

class Doutu1Spider(scrapy.Spider):
    name = 'doutu2'
    allowed_domains = ['doutula.com', "sinaimg.cn"]
    start_urls = ['https://www.doutula.com/photo/list/?page=1']


    def parse(self, response):
        print('----------当前页数是--->第{}页-----------'.format(response.request.url.split("=")[-1]))
        urls = re.findall('data-original="(.*?)"',response.text, re.S)
        img_names = re.findall('alt="(.*?)"', response.text, re.S)
        for url, img_name in zip(urls, img_names):
            yield scrapy.Request(
                url,
                meta={'img_name': img_name},
                callback=self.download
            )

        next_url = response.xpath('//a[text()="›"]/@href').get()
        print(next_url)
        if next_url:
            yield response.follow(
                next_url,
                callback=self.parse
            )


    def download(self, response):
        item = {}
        item["img"] = response.body
        item["img_name"] = response.meta['img_name']
        print("{url}, {img_name}, 抓取成功".format(url=response.request.url, img_name=item["img_name"]))
        yield item
