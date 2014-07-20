from django.contrib import admin

# Register your models here.
from django.contrib import admin
from webstore.models import Category, Product, Inventories, Picture, SalesPrice

## Inlines

class SalesPriceInline(admin.TabularInline):
	model = SalesPrice
	extra = 1

class InventoriesInline(admin.TabularInline):
	model = Inventories
	extra = 1

class PictureInline(admin.TabularInline):
	model = Picture
	extra = 1

## Admins

class InventoriesAdmin(admin.ModelAdmin):
	inlines = [SalesPriceInline]
	#verbose_name_plural = 'Inventories'

class ProductAdmin(admin.ModelAdmin):
	fields = ['name', 'category', 'gender', 'price_purchased', 'price_recommended']
	inlines = [InventoriesInline, PictureInline]

	list_display = ('name', 'category','gender', 'price_recommended')
	
	list_filter = ['category__name', 'gender']

	search_fields = ['name']

	#save_on_top = True


admin.site.register(Product, ProductAdmin)
