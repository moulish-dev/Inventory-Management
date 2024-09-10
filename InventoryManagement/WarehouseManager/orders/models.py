from django.db import models

# Create your models here.

class Products(models.Model):
    
    code = models.CharField( max_length=50, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    type = models.CharField(max_length=30)
    brand = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    stock = models.IntegerField(max_length=100, null=True)
    product_color = models.CharField(max_length = 30, null=True)


class ShopAdmin(models.Model):

    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=30)


class Orders(models.Model):

    shop_id = models.ForeignKey(ShopAdmin, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):

    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    quantity_type=models.CharField(max_length=20)
