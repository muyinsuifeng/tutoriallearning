# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DemoItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class SingerItem(scrapy.Item):
    song_name_link = scrapy.Field()
    song_name = scrapy.Field()
    song_mv_link = scrapy.Field()
    song_artist_name_link = scrapy.Field()
    song_artist_name = scrapy.Field()
    song_album_name_link = scrapy.Field()
    song_album_name = scrapy.Field()
