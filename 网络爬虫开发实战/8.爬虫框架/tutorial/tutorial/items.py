# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 这里创建了一个爬取数据的容器，定义了一些必要的字段
class QuoteItem(scrapy.Item):
    # 文本信息
    text = scrapy.Field()
    # 作者信息
    author = scrapy.Field()
    # 标签信息
    tags = scrapy.Field()
