import scrapy
import json
from ..items import MonsoonItem


class MonsoonSpider(scrapy.Spider):
    name = "monsoon"
    #allowed_domaind = ["www.monsoonlondon.com"]
    #start_urls = ['https://www.monsoonlondon.com']

    '''def parse (self,response):
        #categories = response.xpath('//*[@id="mainNavLinks"]/li/a/@href').extract()
        categories = response.xpath('//*[@id="mainNavLinks"]/li/div/ul/li/ul/li/a/@href') #.extract()
        for href in categories:
            link = response.urljoin(href.extract())
            yield link  #{'category': link}'''

    '''def parse(self,response):
        url_next = response.xpath('//link[@rel="next"]/@href').extract()
        print(url_next)
        for href in response.xpath('//*[@id="mainNavLinks"]/li/div/ul/li/ul/li/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url,callback=self.parse)
            #print(url_next)'''

    #def parse(self, response):
    monsoon_base_url = "https://www.monsoonlondon.com/en-ua/view/services/getProducts.json?pageSize=12&sort=newIn&page=1&category=mon_1.2"
    #monsoon_base_url = "https://www.monsoonlondon.com/en-ua/women/dresses?pageSize=12&page=1&showAll=&sort=score"
    start_urls = [monsoon_base_url]
    page = 2
    download_delay = 1.5

    def parse(self, response):
        data = json.loads(response.body.decode('utf-8'))

        items = MonsoonItem()
        for item in data.get('results'):
            #print(data)
            items['name'] = item.get('name')
            items['id'] = item.get('id')
            items['price'] = item.get('price')
            items['productUrl'] = item.get('productUrl')
            yield items #{
                #'name': item.get('name'),
                #'id': item.get('id'),
                #'price': item.get('price'),
                #'productUrl': item.get('productUrl')
            #}
        next_page = 'https://www.monsoonlondon.com/en-ua/view/services/getProducts.json?pageSize=12&sort=newIn&page='+str(MonsoonSpider.page)+'&category=mon_1.2'
        #next_page = 'https://www.monsoonlondon.com/en-ua/women/dresses?pageSize=12&page='+str(MonsoonSpider.page)+'&showAll=&sort=score'
        if MonsoonSpider.page < 21:
            MonsoonSpider.page +=1
            #next_page = item['currentPage']+1
            yield response.follow(next_page, callback=self.parse)

                #yield scrapy.http.Request(url,callback=self.parse)

    #def parse_page(self,response):

