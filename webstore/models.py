# coding=utf8
from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(u'類別名稱', max_length = 10)

	def __unicode__(self):
		return self.name

class Product(models.Model):
	GENDER = (
		('F', u'女'),
		('M', u'男'),
		('U', u'不限')
		)

	name = models.CharField(u'商品名稱', max_length = 20)
	category = models.ForeignKey(Category, verbose_name= u'類別')
	price_purchased = models.IntegerField(u'進價') 
	price_recommended = models.IntegerField(u'建議售價/定價')
	gender = models.CharField(u'性別', max_length = 1, choices = GENDER)
	num_views = models.IntegerField(u'瀏覽次數',default=0)

	def __unicode__(self):
		return self.name

class Inventories(models.Model):
	product = models.ForeignKey(Product, verbose_name = u'商品名稱')
	size = models.CharField(u'大小', max_length = 3)
	color = models.CharField(u'顏色', max_length = 5)
	num_in_stock = models.IntegerField(u'庫存量')
	num_sold = models.IntegerField(u'已售', default = 0)
	serial_number = models.CharField(u'商品編號', max_length = 20)
	date = models.DateTimeField(u'上傳日期')

	def __unicode__(self):
		return '\t'.join([self.size, self.color, self.serial_number]);

class Picture(models.Model):
	product = models.ForeignKey(Product, verbose_name = u'商品名稱')
	##TODO: possibly using Image Field
	url = models.URLField(u'圖片連結', max_length = 2048)

	def __unicode__(self):
		return "";

class SalesPrice(models.Model):
	product = models.ForeignKey(Product, verbose_name = u'商品名稱')
	inventory = models.ForeignKey(Inventories, verbose_name = u'庫存')
	price_sold = models.IntegerField(u'賣出價') 

	def __unicode__(self):
		#return self.inventory.__unicode__()
		return ""

