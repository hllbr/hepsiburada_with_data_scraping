import scrapy
from ..items import HepsiburadaItem

class HepsiburadaTutorial(scrapy.Spider):
    name = 'hepsiburada'
    
    start_urls = [
        'https://www.hepsiburada.com/bilgisayarlar-c-2147483646'
    ]
    page_number = 2
    def parse(self,response):
        items = HepsiburadaItem()

        prod_name = response.xpath("//li/div/a/div[@class='product-detail']/h3/@title").extract()

        prod_old_price = response.xpath("//li/div/a/div[@class='product-detail']/div/del/text()").extract()

        prod_new_price = response.xpath("//li/div/a/div[@class='product-detail']/div/span[@class='price old product-old-price']/text() | //li/div/a/div[@class='product-detail']/div/span[@class='price old product-old-price']/text()").extract()

        prod_discount_price = response.xpath("//li/div/a/div[@class='product-detail']/div/div[@class='price-value']/text()").extract()

        prod_photo = response.xpath("//li/div/a/div[@class='product-image-wrapper']/figure/div/img/@data-src").extract()

        product_review_no = response.xpath("//li/div/a/div[@class='product-detail']/div/span[@class='number-of-reviews']/text()").extract()

        prod_url = response.xpath("//li[@class='search-item col lg-1 md-1 sm-1  custom-hover not-fashion-flex']/div/a/@href").extract()

        # Assigning values to the key in the items object
        items['prod_name'] = prod_name
        items['prod_old_price'] = prod_old_price
        items['prod_new_price'] = prod_new_price
        items['prod_discount_price'] = prod_discount_price
        items['prod_photo'] = prod_photo
        items['product_review_no'] = product_review_no
        items['prod_url'] = prod_url

        yield items

        next_page = "https://www.hepsiburada.com/bilgisayarlar-c-2147483646?sayfa={}".format(HepsiburadaTutorial.page_number)
        if next_page:
            

            HepsiburadaTutorial.page_number += 1
            yield response.follow(next_page, callback=self.parse)
    
