# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HepsiburadaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    prod_name = scrapy.Field() 
    prod_old_price = scrapy.Field()
    prod_new_price = scrapy.Field()
    prod_discount_price = scrapy.Field()
    prod_photo = scrapy.Field()
    product_review_no = scrapy.Field()
    prod_url = scrapy.Field()
