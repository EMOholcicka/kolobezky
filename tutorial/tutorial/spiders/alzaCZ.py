import scrapy
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import datetime
import re

class KolobkyCZspider(scrapy.Spider):
    name = "AlzaCZ"
    start_urls = [
		'https://www.alza.cz/sport/kolobezky-na-dlouhe-trasy/18865181.htm',
		]

    def parse(self, response):
        ###select wide for item per single page
        SET_SELECTOR = '.box'
        ###today section###
        mylist = []
        today = datetime.date.today()
        mylist.append(today)
        for brickset in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'a ::text'
            PRICE_SELECTOR = '.c2 ::text'
            PRICE_SELECTOR1 = re.sub('[^A-Za-z0-9]+', '', brickset.css(PRICE_SELECTOR).extract_first())
            yield {
                'date': mylist[0],
                'eshop': "Alza.cz",
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'price': PRICE_SELECTOR1,
		}


