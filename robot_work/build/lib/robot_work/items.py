# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RobotWorkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MusicListItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    play = scrapy.Field()
    user = scrapy.Field()


class MusicDetailItem(scrapy.Item):
    title = scrapy.Field()
    tag = scrapy.Field()
    description = scrapy.Field()
    collection = scrapy.Field()
    play = scrapy.Field()
    songs = scrapy.Field()
    comments = scrapy.Field()
