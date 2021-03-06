# -*- coding: utf-8 -*-
import scrapy
from maoyan_spider.items import MaoyanSpiderItem
from scrapy.selector import Selector

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        movies = Selector(response=response).xpath('//dd/div[2]/a/@href')
        for i in range(0,10):
            url = f'https://maoyan.com' + movies[i].extract()
            yield scrapy.Request(url=url,callback=self.parse2, dont_filter=False)

    # 解析函数
    def parse2(self, response):
        # 打印网页的url
        print(response.url)

        movie = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        for tag in movie:
            item = MaoyanSpiderItem()
            title = tag.xpath('./h1/text()').extract()
            date = tag.xpath('./ul/li[2]/text()').extract()
            print(title, date)
            item['title'] = title
            item['date'] = date
            yield item

