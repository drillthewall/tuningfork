# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PitchforkScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    album = scrapy.Field()
    artist = scrapy.Field()
    year = scrapy.Field()
    score = scrapy.Field()
    genre = scrapy.Field()
    reviewer = scrapy.Field()
    text = scrapy.Field()
    italic = scrapy.Field()
    links = scrapy.Field()
    artistLinks = scrapy.Field()
    albumLinks = scrapy.Field()