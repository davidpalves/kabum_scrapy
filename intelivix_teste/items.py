# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KabumItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    category = scrapy.Field()
    brand = scrapy.Field()
    navigation = scrapy.Field()
    vendor_name = scrapy.Field()
    current_price = scrapy.Field()
    discount_price = scrapy.Field()
    main_image = scrapy.Field()
    secondary_images = scrapy.Field()
    features = scrapy.Field()

