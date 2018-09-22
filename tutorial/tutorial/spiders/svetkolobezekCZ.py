import scrapy
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import datetime
import re

class SvetkolobezekCZspider(scrapy.Spider):
    name = "SvetkolobezekCZ"
    start_urls = [
                'https://www.svetkolobezek.cz/kolobezky/yedoo/',
		'https://www.svetkolobezek.cz/kolobezky/mibo/', 
		'https://www.svetkolobezek.cz/kolobezky/morxes/',               
                ]

    def parse(self, response):
        ###select wide for item per single page
        SET_SELECTOR = '.vypis-zbozi'

        ###today section###
        mylist = []
        today = datetime.date.today()
        mylist.append(today)

        for brickset in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'h3 a ::text'
            PRICE_SELECTOR = 'strong ::text'
            PRICE_PARSER = re.sub('[^A-Za-z0-9]+', '', brickset.css(PRICE_SELECTOR).extract_first().replace("K", ""))
            NAME_PARSER = brickset.css(NAME_SELECTOR).extract_first().replace(" koloběžka", "")
            yield {
                'date': mylist[0], 
                'eshop': "svetkolobezek.cz",
                'name': NAME_PARSER,
                'price': PRICE_PARSER,
                }



