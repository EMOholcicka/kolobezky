import scrapy

class AlzaCZspider(scrapy.Spider):
    name = "AlzaCZ"
    start_urls = [
            'https://www.alza.cz/sport/yedoo-wolfer?dq=4826750',
            ]

    def parse(self, response):
        for item in response.css('div.breadCrupmps'):
            naming = response.css('div.breadCrupmps')
            main = response.css('div.canBuy')
            yield {
                'shop': 'Alza.cz', 
                'name': naming.css('a.last').extract_first().split(">")[-2].split("<")[0],
                'cena': main.css('span.price_withVat').extract_first().split(">")[1].split(",")[0],
                }
