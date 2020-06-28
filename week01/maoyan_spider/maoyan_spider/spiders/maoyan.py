# -*- coding: utf-8 -*-
import scrapy
from maoyan_spider.items import MaoyanSpiderItem
from scrapy.selector import Selector

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        movies = Selector(response=response).xpath('//dd')
        for i in range(0,10):
            link = movies[i].xpath('./div[2]/a/@href')
            url = f'https://maoyan.com/films?showType=3' + link
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    # 解析函数
    def parse(self, response):
        # 打印网页的url
        print(response.url)

        movie = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        for tag in movie:
            title = tag.xpath('./h1/text()')
            date = tag.xpath('./ul/li[2]/text()')
            item = response.meta['item']
            item['title'] = title
            item['date'] = date
            yield item

