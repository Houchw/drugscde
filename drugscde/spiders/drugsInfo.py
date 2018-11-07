# -*- coding: utf-8 -*-
import scrapy
from drugscde.items import DrugscdeItem


class DrugsinfoSpider(scrapy.Spider):
    name = "drugsInfo"
    allowed_domains = ['cde.org.cn']
    start_urls = ["http://www.cde.org.cn/transparent.do?method=list&year=2018&currentPageNumber=1&checktype=1&statenow=0"]

    def parse(self, response):
        page = response.xpath('//td[@id="pageNumber"]/font/text()').extract()[1].strip()
        page = int(page)+1
        #year = u"全部"
        statenow = 0 # 0为收审记录，1为在审记录，记得在更改时调整start_urls.
        urls = "http://www.cde.org.cn/transparent.do?method=list&year=2018&currentPageNumber={page}&checktype=1&statenow={statenow}"
        for p in range(1, page):
            url = urls.format(page = p, statenow = statenow)
            yield scrapy.Request(url = url, callback = self.parse_page)

    def parse_page(self, response):
        table = response.xpath('//table')[6]
        try:
            for tr in table.xpath('./tr'):
                item = DrugscdeItem()
                tds = tr.xpath('./td')
                tmp = []

                for td in tds:
                    ext_data = td.xpath('concat(./text(), " ")').extract_first()
                    tmp.append(ext_data)

                tds = tmp
                item["app_no"] = tds[0].strip()
                item["drug_name"] = tds[1].strip()
                item["drug_type"] = tds[2].strip()
                item["app_type"] = tds[3].strip()
                item["inv_type"] = tds[4].strip()
                item["corp_name"] = tds[5].strip()
                item["rec_date"] = tds[6].strip()

                yield item
        except:
            pass
