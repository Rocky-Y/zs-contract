# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from ..items import ZsItem


class ContractSpider(scrapy.Spider):
    name = 'contract'
    allowed_domains = ["202.96.189.107"]
    start_url = []
    with open('C:/Users/Administrator/Desktop/wangqian_test -2.csv') as fh:
        line = fh.readlines()
        for li in line:
            li = li.split(',')[8]
            start_url.append(li)

    def parse(self, response):
        # print(len(response.text))

        item = ZsItem()
        tr = Selector(response).xpath('//tr[contains (@class, "listrow")]')
        if tr:
            # 项目名称
            item['name'] = Selector(response).xpath('//span[@id="ctl00_ContentPlaceHolder1_Layout1_Label1"]/text()').extract()[0]
            # 所在镇区
            item['town'] = Selector(response).xpath('//span[@id="ctl00_ContentPlaceHolder1_Layout1_Label2"]/text()').extract()[0]
            # 企业名称
            item['firm'] = Selector(response).xpath('//span[@id="ctl00_ContentPlaceHolder1_Layout1_Label3"]/text()').extract()[0]
            # 项目地址
            item['site'] = Selector(response).xpath('//span[@id="ctl00_ContentPlaceHolder1_Layout1_Label4"]/text()').extract()[0]
            # 预售证号
            item['card'] = Selector(response).xpath('//span[@id="ctl00_ContentPlaceHolder1_Layout1_Label5"]/text()').extract()[0]
            # 批准日期
            item['date'] = Selector(response).xpath('//span[@id="ctl00_ContentPlaceHolder1_Layout1_Label6"]/text()').extract()[0]
            # 预售证有效期
            item['term'] = Selector(response).xpath('//span[@id="ctl00_ContentPlaceHolder1_Layout1_Label7"]/text()').extract()[0]


            item['building_list'] = []
            for conn in tr:
                # 销售状态
                state = conn.xpath('./td[@align="center"][1]/span/text()').extract()
                # 楼号
                number = conn.xpath('./td[@align="center"][2]/span/text()').extract()
                # 批准销售套数
                approve = conn.xpath('./td[@align="center"][3]/span/text()').extract()
                # 已销售套数
                sale = conn.xpath('./td[@align="center"][4]/span/text()').extract()
                # 可销售套数
                rest = conn.xpath('./td[@align="center"][5]/span/text()').extract()
                # 开工日期
                start = conn.xpath('./td[@align="center"][6]/span/text()').extract()
                # 竣工日期
                complete = conn.xpath('./td[@align="center"][7]/span/text()').extract()
                # 终止次数
                stop = conn.xpath('./td[@align="center"][8]/span/text()').extract()
                # 楼盘表
                url_ = conn.xpath('./td[@align="center"][9]/a/@href').extract()[0].split("'")[1]
                url = 'http://202.96.189.107:9043/' + url_
                # .split("'")[1]
                list_ = (state, number, approve, sale, rest, start, complete, stop, url)
                item['building_list'].append(list_)

            yield item




