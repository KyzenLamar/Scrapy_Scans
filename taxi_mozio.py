import scrapy
import json
import base64
from scrapy_splash import SplashRequest
from ..items import TaxiItem
import csv


class MozioSpider(scrapy.Spider):
    name = 'mozio'


    # THE INPUT FILE WHERE NEEDED DATE WILL BE CHANGED
    '''with open('mozio_links.csv','r',encoding='utf-8') as links:
        for line in links:
            link = line.replace('06%2F19%2F2020','07%2F19%2F2020')
            file = open('actual_date_links.csv','a',encoding='utf-8')
            file.write(link)
            file.close()'''

    #def start_links(Booking , index = 0 ,ignor_headers=True):
    # with open('Booking_EX.csv','r',encoding='utf-8') as urls:
    #     start_urls = [url.strip() for url in urls.readlines()]
        # file = open('Booking_EX.csv', 'r', encoding='utf-8')
        # fildname = ['routs', 'links']
        # inputFile = csv.DictReader(file)
        # start_urls = []
        # temp = {}
        # for row in inputFile:
        #     temp['link'] = row["links"]
        #     temp['routs'] = row["routs"]
        #     start_urls.append(temp)
    routs = []
    start_urls =[]
    with open('Booking_EX.csv','r',encoding='utf-8') as urls:
        reader = csv.reader(urls)
        for i, row in enumerate(reader):
            routs.append(row[0])
            start_urls.append(row[1])
        #print(routs)
        #print(start_urls)
            #return routs


    def start_requests(self):

        for key,value in enumerate(self.start_urls):
            global rout
            rout = self.routs[key]
            # print('=============')
            # print(rout)
            # print('=============')
            splash_args = {'html': 1,
                           'png': 1,
                           'wait': 9,
                           'render_all': 1,
                           'rout': rout}

            yield SplashRequest(url=value +','+rout, callback=self.parse, endpoint='render.html',body=rout, args=splash_args)


    def parse(self, response):

        #price = response.xpath()
        items = TaxiItem()
        # pick_up = response.xpath('//dd[@data-test="tx-trip-summary__pickup-text"]/text()').get()
        # drop_off = response.xpath('//dd[@data-test="tx-trip-summary__dropoff-text"]/text()').get()

        # imgdata = base64.b64decode(response.data['png'])
        # screen = 'booking_image' + '_' + drop_off + '.png'
        # with open(screen, 'wb') as f:
        #     f.write(imgdata)

        #price = response.xpath("//*[@class='gb-c-carousel__item']//*[@data-test='gb-price-value]/text()").getall() #//*[@data-test='gb-price-value']
        #price = response.xpath("//*[@data-test='tx-transport-item__accessible-passengers-text']/text()").get()
        #price = response.xpath('//span[contains(@data-test,"tx-transport-item__accessible-passengers-text")]/text()').getall()
        price = response.xpath('//div[@class="gb-c-carousel__item"][contains(.,"Standard")and(contains(.,"Up to 3"))and(contains(.,"Meet & Greet"))]//div[@data-test="gb-price-value"]/text()').get()
        price_for_4 = response.xpath('//div[@class="gb-c-carousel__item"][contains(.,"Standard")and(contains(.,"Up to 4"))and(contains(.,"Meet & Greet"))]//div[@data-test="gb-price-value"]/text()').get()
        price_for_5 = response.xpath('//div[@class="gb-c-carousel__item"][contains(.,"Standard")and(contains(.,"Up to 5"))and(contains(.,"Meet & Greet"))]//div[@data-test="gb-price-value"]/text()').get()
        price_for_6 = response.xpath('//div[@class="gb-c-carousel__item"][contains(.,"Standard")and(contains(.,"Up to 6"))and(contains(.,"Meet & Greet"))]//div[@data-test="gb-price-value"]/text()').get()

        items['price'] = price
        items ['routs'] = response.url.split(',')[1]
        items['link'] = response.url.split(',')[0]
        items['price_for_4'] = price_for_4
        items['price_for_5'] = price_for_5
        items['price_for_6'] = price_for_6
        #items['drop_off'] = drop_off


        yield items