# -*- coding: utf-8 -*-
import scrapy


class CsdnSpider(scrapy.Spider):
    name = "csdn"
    allowed_domains = ["csdn.net"]
    start_urls = (
        'http://blog.csdn.net/',
    )

    def parse(self, response):
        pass
