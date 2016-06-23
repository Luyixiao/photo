# coding=gbk
from scrapy.spiders import Spider  
from scrapy.selector import Selector  
import scrapy
#from scrapy import log  
  
from photo.items import PhotoItem  
  
  
class photoSpider(Spider):  
    name = "photoSpider"  
    start_urls = [  
        "http://car.autohome.com.cn/pic/" 
    ]  #start url at the first page
    
    def parse(self, response): #这个是spider类中默认的方法，我们做一个重写，response就是那个html文件哦。
        item = PhotoItem() 
        sel = Selector(response)#“html”文件被转化成了一个Selector（选择器）对象哦。这个对象的好处是，可以接受xpath或者css。
        sites = sel.xpath("//img/@src").extract()
        for siteUrl in sites: 
            print siteUrl
            item['url'] = siteUrl
            print "lyx"+siteUrl
            yield item
            
            