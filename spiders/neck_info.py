# Scrape the website https: // www.houseofindya.com / for list of necklace sets under jewelry and corresponding description, price and image urls. You must use scrapy for this and create output in csv and json formats. and requirements.txt

import scrapy
from ..items import NecklaceItem


class necklace_set_scrape(scrapy.Spider):
    name = 'necks'
    start_urls = ['https://www.houseofindya.com/zyra/necklace-sets/cat']

    def parse(self, response):
        cata = response.css("ul#JsonProductList li::attr(data-url)").extract()
        for necklace in cata:
            yield scrapy.Request(necklace,callback=self.parse_main)
    
    def parse_main(self, response):
        
        items=NecklaceItem()

        main_box=response.css("div.prodBox")
        info_box = main_box.css("div.prodRight")

        items['name'] = info_box.css("h1::text").extract()[0]
        items['img_urls']=main_box.css("li.zoomli a::attr(data-image)").extract()
        items['price'] = info_box.css("h4 span:nth-child(3)::text").extract()[0][1:]
        items['desc'] = "".join(info_box.css("div#tab-1 p::text").extract())

        yield items
        # yield {'Name': name, 'Description': description,'Price': price, 'Image URLs': im_list}
