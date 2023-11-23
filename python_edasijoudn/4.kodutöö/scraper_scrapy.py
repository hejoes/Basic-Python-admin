 
import scrapy

class ProductSpider(scrapy.Spider):
    name = 'product_spider'
    start_urls = ['https://scrapeme.live/shop/']

    # Function extracts current page information
    def parse(self, response):
        for product in response.css('ul.products li'):
            yield {
                'Title': product.css('h2.woocommerce-loop-product__title::text').get(),
                'price': product.css('.woocommerce-Price-amount::text').get(),
                'Picture href': product.css('img::attr(src)').get(),
            }

        # Extract next page url
        next_page_url = response.css('a.next::attr(href)').get()
        if next_page_url:
            yield response.follow(next_page_url, callback=self.parse)