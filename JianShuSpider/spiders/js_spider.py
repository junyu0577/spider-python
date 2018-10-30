# -*- coding: utf-8 -*-
import scrapy
from JianShuSpider.items import JianshuspiderItem
import re


class JsSpiderSpider(scrapy.Spider):
    name = 'js_spider'
    allowed_domains = ['www.jianshu.com/c/9ca077f0fae8?order_by=added_at']
    start_urls = ['https://www.jianshu.com/c/9ca077f0fae8?order_by=added_at']

    def parse(self, response):

        page = 2

        if ('page' in response.url):
            page = int(response.url[response.url.index('page') + 5::])
            page += 1

        article_list = response.xpath("/html/body/div/div/div/div/ul/li/div")

        if (201 == page):
            print("--------over--------")
            return

        print("--------第" + str(page) + "页--------")

        for item in article_list:
            js_item = JianshuspiderItem()
            js_item['title'] = item.xpath('./a/text()').extract_first()
            js_item['author'] = item.xpath('./div/a/text()').extract_first()
            js_item['link'] = "https://www.jianshu.com" + item.xpath('./a/@href').extract_first()

            print(js_item['title'], end='    ')
            print(js_item['author'], end='    ')
            print(js_item['link'])

        yield scrapy.Request(
            "https://www.jianshu.com/c/9ca077f0fae8?order_by=added_at&page=" + str(page),
            callback=self.parse, dont_filter=True)
