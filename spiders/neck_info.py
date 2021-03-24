# Scrape the website https: // www.houseofindya.com / for list of necklace sets under jewelry and corresponding description, price and image urls. You must use scrapy for this and create output in csv and json formats. and requirements.txt

import scrapy


class BlogSpider(scrapy.Spider):
    name = 'necks'
    start_urls = ['https://www.houseofindya.com/zyra/necklace-sets/cat']

    def parse(self, response):
        # for image along with title: response.css(".lazy")[0].extract()
        # for price: #JsonProductList span:nth-child(1)::text
        # cata:   cata=response.css("ul#JsonProductList")
        # yield {'Title demo':response.css('title::text').extract()}
        # for title in response.css('.oxy-post-title'):
        #     yield {'title': title.css('::text').get()}

        # for next_page in response.css('a.next'):
        #     yield response.follow(next_page, self.parse)
        cata = response.css("ul#JsonProductList li::attr(data-url)").extract()
        for necklace in cata:
            yield scrapy.Request(necklace,callback=self.parse_main)
            # yield {'link': necklace.css("li::attr(data-url)").extract()}
            # yield {'images': im}
    
    def parse_main(self, response):
        main_box=response.css("div.prodBox")
        info_box = main_box.css("div.prodRight")

        name = info_box.css("h1::text").extract()[0]
        im_list=main_box.css("li.zoomli a::attr(data-image)").extract()
        price = info_box.css("h4 span:nth-child(3)::text").extract()[0][1:]
        description = "".join(info_box.css("div#tab-1 p::text").extract())

        yield {'Name':name,'Price':price,'image urls': im_list,'Description':description}
