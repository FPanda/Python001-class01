# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# 注册到settings.py文件的ITEM_PIPELINES中，激活组件
class MaoyanSpiderPipeline:
    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        title = item['title']
        types = item['types']
        date = item['date']
        output = f'|{title}|\t|{types}|\t|{date}|\n\n'
        with open('./maoyan_movie.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item

