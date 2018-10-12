# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class ZsPipeline(object):
    def process_item(self, item, spider):
        # conn = pymysql.connect(host="127.0.0.1", user="root", passwd="admin", db="zhongshan")
        with open('C:/Users/Administrator/Desktop/3.csv', 'w', encoding='utf-8-sig') as fh3:

            # 项目名称
            name = item['name']
            # 所在镇区
            town = item['town']
            # 企业名称
            firm = item['firm']
            # 项目地址
            site = item['site']
            # 预售证号
            card = item['card']
            # 批准日期
            date = item['date']
            # 预售证有效期
            term = item['term']
            # 详细信息列表
            building_list = item['building_list']

            fh3.write("{},{},{},{},{},{},{},{}\n".format(name, town, firm, site, card, date, term, building_list))

        fh3.close()
        return item

        # sql = "INSERT INTO loupan(name_, town, firm, site, card, date_, term, building_list ) VALUES ('" + name + "','" + town + "','" + firm + "','" + site + "','" + card + "','" + term + "','" + building_list + "')"
        # conn.query(sql)
        # conn.close()
        # return item



