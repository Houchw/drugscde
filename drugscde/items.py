# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DrugscdeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    app_no = scrapy.Field()
    drug_name = scrapy.Field()
    drug_type = scrapy.Field()
    app_type = scrapy.Field()
    inv_type = scrapy.Field()
    corp_name = scrapy.Field()
    rec_date = scrapy.Field()
