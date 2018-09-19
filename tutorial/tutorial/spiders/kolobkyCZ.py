import scrapy
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import datetime
import re

class KolobkyCZspider(scrapy.Spider):
    name = "KolobkyCZ"
    start_urls = [
                'https://kolobky.cz/obchod/kolobezka-morxes-sport/',                
                'https://kolobky.cz/obchod/kolobezka-kickbike-race-max-28/',
                'https://kolobky.cz/obchod/kolobezka-mibo-gs/'
                'https://kolobky.cz/obchod/kolobezka-yedoo-trexx/',
                'https://kolobky.cz/obchod/kolobezka-morxes-imola/',
		'https://kolobky.cz/obchod/kolobezka-mibo-gs/',
                ]

    def parse(self, response):
        ###select wide for item per single page
        SET_SELECTOR = '.summary'
        ###today section###
        mylist = []
        today = datetime.date.today()
        mylist.append(today)
        for brickset in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'h1 ::text'
            PRICE_SELECTOR = '.price ::text'
            PRICE_PARSER = re.sub('[^A-Za-z0-9]+', '', brickset.css(PRICE_SELECTOR).extract_first().replace(",00", ""))
            PRICE_SELECTOR1 = re.sub('[^A-Za-z0-9]+', '', brickset.css(PRICE_SELECTOR).extract_first())
            yield {
                'date': mylist[0], 
                'eshop': "Kolobky.cz",
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'price': PRICE_PARSER
                }



