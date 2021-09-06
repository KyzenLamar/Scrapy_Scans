import scrapy
from scrapy_splash import SplashRequest
from ..items import markItem
import csv
from scrapy import Selector

class msfoodSpider(scrapy.Spider):
    name = "msfood"
    with open('Marks_Food_links.csv','r',encoding='utf-8') as urls:
        start_urls = [url.strip() for url in urls.readlines()]

    def start_requests(self):
        # for url in self.start_urls:
        #     print(url)
        #
        #     yield scrapy.http.Request(url=url)
        for url in (self.start_urls):
            #global rout
            #rout = self.routs[key]
            # print('=============')
            # print(rout)
            # print('=============')
            splash_args = {'html': 1,
                           'png': 1,
                           'wait': 9,
                           'render_all': 1
                           }

            yield SplashRequest(url=url, callback=self.parse, endpoint='render.html', args=splash_args)


    def parse(self, response):
        items = markItem()
        # resultlist =[]
        # productId = response.xpath('//*[@type="text/javascript"][(contains(. , "productInformation.push"))]').extract()
        # for sku in productId:
        #     sku = sku.replace('productInformation.push(','').split(',')
        #     for resaltsku in sku:
        #         resaltsku.replace('[','').replace(']','').replace("'",'"').replace('"variants":[', '').replace("'product' : ", '')
        #         if '[{"id":' in resaltsku:
        #             resultlist.append(resaltsku)

        sizes = response.xpath('//*[@class = "sizes"]//label[not(contains (@class, "no-stock"))]/text()').extract()
        for size in sizes:
            size = size
            with open('FCUK.csv','a',  encoding='utf-8') as output:
                headers = ['size','url']
                writer = csv.DictWriter(output, fieldnames=headers)
                writer.writerow({'url': response.url, 'size': size})


        items['productSize'] = sizes
        items['productLink'] = response.url


        yield items

