import scrapy
import re
from scrapy.http import Request
from spiders.items import YkkItem
class MySpider(scrapy.Spider):

    name = 'demo'
    start_urls = ["http://yyk.99.com.cn/beijing/"]
    base_url = "http://yyk.99.com.cn"
    def parse(self,response):
        for href in response.css('.tablist a::attr(href)').extract():
            yield scrapy.Request(href,callback=self.parse_info)
        
    def parse_info(self, response):
        item = YkkItem()
        item["city"]=response.xpath('/html/body/div[5]/div[1]/p/a[2]/text()').extract()
        item['area']=response.xpath('/html/body/div[5]/div[1]/p/a[3]/text()').extract()
        name=response.xpath('/html/body/div[5]/div[2]/h1/text()').extract()
        item['name'] = [name[0].strip()]
        item['nickname']=response.xpath('/html/body/div[5]/div[3]/div[1]/div[2]/div[2]/ul/li[1]/span/text()').extract()
        item['rank']=response.xpath('/html/body/div[5]/div[3]/div[1]/div[2]/div[2]/ul/li[3]/span/text()').extract()
        item['telephone']=response.xpath('/html/body/div[5]/div[3]/div[1]/div[2]/div[2]/ul/li[4]/span[1]/text()').extract()
        item['address']=response.xpath('/html/body/div[5]/div[3]/div[1]/div[2]/div[2]/ul/li[5]/span/text()').extract()
        yield item