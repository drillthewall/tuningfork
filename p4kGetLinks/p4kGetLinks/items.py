# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class P4KgetlinksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    reviewURL = scrapy.Field()
    artist = scrapy.Field()
    album = scrapy.Field()
    italic = scrapy.Field()
    