from django.contrib import admin
from .models import Product, Offer, Fruit, Vegetable

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')

class FruitAdmin(admin.ModelAdmin):
    list_display = ('Price', 'Quantity_Stock')



class VegetableAdmin(admin.ModelAdmin):
    list_display = ('price_Vegetable', 'stock_Vegetable')


admin.site.register(Offer,OfferAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Fruit, FruitAdmin)
admin.site.register(Vegetable, VegetableAdmin)