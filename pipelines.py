# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector
class AmazonPipeline(object):

	def __init__(self):
		self.create_connection()
		self.create_table()

	def create_connection(self):
		self.conn = mysql.connector.connect(
			host = 'localhost ',
			user = 'root ',
			passwd = 'Shobhit123@',
			database = 'laptop'
			)
		self.curr = self.conn.cursor()

	def create_table(self):
		self.curr.execute("""DROP TABLE IF EXISTS amazon_tb""") 
		self.curr.execute("""create table amazon_tb(
	         product_name text,
	         product_price text,
	         product_imagelink text
	         )""")
	def process_item(self, item, spider):
		self.store_db(item)
		print("Pipeline: " + item['product_name'][0])
		return item

	def store_db(self,item):
		self.curr.execute("""insert into amazon_tb values (%s,%s,%s) """,(
			item['product_name'][0],
			item['product_price'][0],
			item['product_imagelink'][0]
			))
		self.conn.commit()
