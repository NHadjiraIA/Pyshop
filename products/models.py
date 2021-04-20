from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Fruit(models.Model):
    Name_fruit = models.CharField(max_length=255)
    Price = models.FloatField()
    Quantity_Stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Vegetable(models.Model):
    name_Vegetable = models.CharField(max_length=255)
    price_Vegetable = models.FloatField()
    stock_Vegetable = models.IntegerField()
    image_url_Vegetable = models.CharField(max_length=2083)

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
