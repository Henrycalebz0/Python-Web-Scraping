import scrapy  # type: ignore

class Stockscrapy(scrapy.Spider):
    name = 'games'
    start_urls = [
        'https://sandbox.oxylabs.io/products/'
    ]

    def parse(self, response):
        for product in response.css('div.product-card'):
            yield {
                'Name' : product.css('h4.title::text').get(),
                'Price' : product.css('div.price-wrapper::text').get(),
                'Genre' : product.css('span.css-1pewyd6::text').get(),
                'Description': product.css('p.description::text').get(),
                }

        next_page = response.css('a[rel="next"]').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
