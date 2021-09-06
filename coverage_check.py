import scrapy
from..items import CoverageItem
import csv


class ConverseSpider(scrapy.Spider):
    name = 'converse'



    with open('Coverage_check.csv','r',encoding='utf-8') as urls:
        start_urls = [url.strip() for url in urls.readlines()]


    def start_requests(self):

        for url in self.start_urls:
            print(url)

            yield scrapy.http.Request(url=url)



    def parse(self , response):
        items = CoverageItem()
        if response.status in [302]:
            link = response.url
            with open('Result.csv', 'a')as f:
                writer = csv.writer(f)
                writer.writerow(link)


    #     items = CoverageItem()
    #
    #     dataskulist = []
    #     linklist = []
    #
    #     deeplink = response.css('a.thumb-link::attr(href)').extract()
    #     #dataitemid = response.css('li.grid-tile div.product-tile::attr(data-itemid)').extract()
    #
    #     # file = open('woman_all_links_2.csv','w')
    #     # fieldnames = ["deeplink", "dataitemid"]
    #     # writer = csv.DictWriter(f,fieldnames=fieldnames)
    #     # writer.writeheader()
    #
    #     # for link in deeplink:
    #     #     link = link.strip(',')
    #     #     linklist.append(link)
    #     #     with open('outlet_all_links.csv','a')as f:
    #     #         #fieldnames = ["deeplink", "dataitemid"]
    #     #         writer = csv.writer(f)
    #     #
    #     #         writer.writerow({link})
    #     # for itemid in dataitemid:
    #     #     itemid = itemid.strip(',')
    #     #     dataskulist.append(itemid)
    #     #     with open('outlet_all_links_2.csv', 'w'):
    #     #         writer.writerow({'dataitemid': itemid})
    #
    #
    #     #dataitemid = response.css('li.grid-tile div.product-tile::attr(data-itemid)').extract()
    #     #file = open('outlet_all_links_2.csv', 'a')
    #     #fieldnames = ["deeplink", "dataitemid"]
    #     #writer = csv.DictWriter(file, fieldnames=fieldnames)
    #     #writer.writeheader()
    #     # for itemid in dataitemid:
    #     #     itemid = itemid.strip(',')
    #     #     writer.writerow({'dataitemid': itemid})
    #
    #     sku = response.css('.product-detail--title__reverse.pdp li.swatch')#::attr(data-sku)')
    #     if sku:
    #         sku = response.css('.product-detail--title__reverse.pdp li.swatch::attr(data-sku)').getall()
    #         # for datasku in sku:
    #         #     datasku = response.xpath('.//@data-sku').extract()
    #         #     dataskulist.append(datasku)
    #             # with open('Result.csv', 'a')as f:
    #             #     writer = csv.writer(f)
    #             #     writer.writerow({dataskulist +' ' + response.url})
    #
    #
    #
    #     skuCustom = response.xpath('//*[@id="pdpMain"]/div/div[2]/div/section/div/section/div[2]/p[1]/span[2]/text()')
    #     if skuCustom:
    #         skuCustom = response.xpath('//*[@id="pdpMain"]/div/div[2]/div/section/div/section/div[2]/p[1]/span[2]/text()').get()
    #         # with open('Result.csv', 'a')as f:
    #         #     writer = csv.writer(f)
    #         #     writer.writerow({skuCustom + ' ' + response.url[items]})
    #
    #
    #
    #
        #for sk in dataskulist:
        #sk = sk.strip(',')
        #items['sku'] = sku
        #items['skuCustom'] = skuCustom
        items['link'] = response.url
    #
        # with open('Result.csv', 'a')as f:
        #     writer = csv.writer(f)
        #     writer.writerow(items['link'])



        yield items