# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 项目名称
    name = scrapy.Field()
    # 所在镇区
    town = scrapy.Field()
    # 企业名称
    firm = scrapy.Field()
    # 项目地址
    site = scrapy.Field()
    # 预售证号
    card = scrapy.Field()
    # 批准日期
    date = scrapy.Field()
    # 预售证有效期
    term = scrapy.Field()

    # 以下详细信息为列表
    building_list = scrapy.Field()
        # # 销售状态
        # state = scrapy.Field()
        # # 楼号
        # number = scrapy.Field()
        # # 批准销售套数
        # approve = scrapy.Field()
        # # 已销售套数
        # sale = scrapy.Field()
        # # 可销售套数
        # rest = scrapy.Field()
        # # 开工日期
        # start = scrapy.Field()
        # # 竣工日期
        # complete = scrapy.Field()
        # # 终止次数
        # stop = scrapy.Field()
        # # 楼盘表
        # url = scrapy.Field()
