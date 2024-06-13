import os
import json
import scrapy 
from pathlib import Path

class BrvmSpider(scrapy.Spider):
    name = 'brvm_spider'

    def start_requests(self):
        urls = [
            'https://www.brvm.org/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):

        top5 = []
        table = response.css('.top-five tbody tr')[:5]
        for trow in table:
            nom_societe = trow.css('td:nth-child(1)::text').get()
            cours = trow.css('td:nth-child(2)::text').get()
            variation = trow.css('td:nth-child(3)::text').get()
            
            top5.append({
                'nom_societe': nom_societe,
                'cours': cours,
                'variation': variation,
            })

        yield {
            'top5': top5,
        }

        
