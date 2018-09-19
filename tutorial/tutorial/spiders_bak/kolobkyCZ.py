import scrapy

class KolobkyCZspider(scrapy.Spider):
    name = "KolobkyCZ"
    start_urls = [
            'https://kolobky.cz/obchod/kolobezka-yedoo-trexx/',
            'https://kolobky.cz/obchod/kolobezka-crussis-road/',
            'https://kolobky.cz/obchod/kolobezka-yedoo-wolfer/',
            'https://kolobky.cz/obchod/kolobezka-kostka-trip-max-g5/',
            'https://kolobky.cz/obchod/kolobezka-morxes-sport/',
            ]

    def parse(self, response):
        for item in response.css('div.summary'):
            yield {
                'shop': response.css('div.headerinnerwrap h1::text').extract_first(),   
                'name': item.css('div.summary h1::text').extract_first(),
                'cena': item.css("span.amount::text").extract_first(),
                }
