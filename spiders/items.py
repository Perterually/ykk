# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YkkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    area = scrapy.Field()
    name = scrapy.Field()
    nickname = scrapy.Field()
    rank = scrapy.Field()
    telephone = scrapy.Field()
    address = scrapy.Field()

