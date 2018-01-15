import scrapy

from color_data.items import ColorDataItem


class ColorDataSpider(scrapy.Spider):
    name = "ColorData"
    allowed_domains = ["datachart.500.com"]
    start_urls = [
        "https://datachart.500.com/ssq/history/newinc/history.php?limit=100000&sort=0"
    ]

    def parse(self, response):
        trs = response.xpath('//*[@id="tdata"]/tr')
        for index, tr in enumerate(trs):
            item = ColorDataItem()
            item['id'] = tr.xpath('td[1]/text()').extract()
            item['red1'] = tr.xpath('td[2]/text()').extract()
            item['red2'] = tr.xpath('td[3]/text()').extract()
            item['red3'] = tr.xpath('td[4]/text()').extract()
            item['red4'] = tr.xpath('td[5]/text()').extract()
            item['red5'] = tr.xpath('td[6]/text()').extract()
            item['red6'] = tr.xpath('td[7]/text()').extract()
            item['blue'] = tr.xpath('td[8]/text()').extract()
            item['date'] = tr.xpath('td[16]/text()').extract()
            yield item

