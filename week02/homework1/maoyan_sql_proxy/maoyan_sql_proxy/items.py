# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanSqlProxyItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    types = scrapy.Field()
    date = scrapy.Field()
    pass