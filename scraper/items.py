# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RecipeItem(scrapy.Item):
    spider = scrapy.Field()
    url = scrapy.Field()
    language = scrapy.Field()
    json = scrapy.Field()
    checksum = scrapy.Field()
    timestamp = scrapy.Field()
