# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log
import sqlite3



class YkkSqlitePipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect('drug.db')
        self.i = 0
    

    def create_table(self):
        sql = 'DROP TABLE IF EXISTS `info`;CREATE TABLE info (id integer PRIMARY KEY AUTOINCREMENT NOT NULL,catenname text(128),packname text(128),producpackleve text(128),producpacknum text(128),groupsetid text(128),groupitemid text(128),producompany text(128),bidcomany text(128),groupsetname text(128),groupitemname text(128),speci text(128),model text(128),perforcompo text(128),packspeci text(128),packmatel text(128),brand text(128),unit text(128),winbidprice text(128),cate text(128),a text(128));'
        self.conn.executescript(sql)

    def inser_db(self,item):
        sql = "INSERT INTO info(catenname, packname, producpackleve, producpacknum, groupsetid,groupitemid,producompany) VALUES (?,?,?,?,?,?,?)"
        self.conn.execute(sql,item)
        self.conn.commit()


    def open_spider(self,spider):
        self.create_table()

    def close_spider(self,spider):
        self.conn.close()

    def process_item(self, item, spider):
        
        city = item['city']
        area = item['area']
        name = item['name']
        nickname = item['nickname']
        rank = item['rank']
        telephone = item['telephone']
        address = item['address']
        self.inser_db((city[0],area[0],name[0],nickname[0],rank[0],telephone[0],address[0]))
        self.i += 1
        print("success,第%d条" % self.i)
