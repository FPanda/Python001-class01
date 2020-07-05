# -*- coding: utf-8 -*-
import scrapy
from maoyan_sql_proxy.items import MaoyanSqlProxyItem
from scrapy.selector import Selector

class MaoyanProxySpider(scrapy.Spider):
    name = 'maoyan_proxy'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        movies = Selector(response=response).xpath('//dd/div[2]/a/@href')
        for i in range(0,10):
            url = f'https://maoyan.com' + movies[i].extract()
            yield scrapy.Request(url=url,callback=self.parse2, dont_filter=False)

    # 解析函数
    def parse2(self, response):
        print("DEBUG: INTERNAL MASSAGE START HERE")
        movie = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        for tag in movie:
            item = MaoyanSqlProxyItem()
            types = {}
            title = tag.xpath('./h1/text()').extract()
            test = tag.xpath('./ul/li[0]')
            for type in tag.xpath('./ul/li[0]/a/text()'):
                print(type.extract())
                types.append(type)
            date = tag.xpath('./ul/li[2]/text()').extract()
            item['title'] = title
            item['types'] = types
            item['date'] = date

            yield item

