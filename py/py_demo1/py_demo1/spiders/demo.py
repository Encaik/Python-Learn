# -*- coding: utf-8 -*-
import scrapy

class DemoSpider(scrapy.Spider):
    name = 'demo'
    #allowed_domains = ['py_demo1.io']
    start_urls = ['http://www.yzu.edu.cn/']

    def parse(self, response):
        page = response.url.split("/")[-2]
        fname = '%s.html' % page
        with open(fname,'wb') as f:
            f.write(response.body)
        self.log('Saved file %s.' % fname)
