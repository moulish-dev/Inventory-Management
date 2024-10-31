from django.db import models

# Create your models here.

class Products(models.Model):
    
    code = models.CharField( max_length=50, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500,null=True, blank=True)
    type = models.CharField(max_length=30,null=True, blank=True)
    brand = models.CharField(max_length=50,null=True, blank=True)
    category = models.CharField(max_length=50,null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    stock = models.IntegerField( null=True, blank=True)
    product_color = models.CharField(max_length = 30, null=True, blank=True)


class ShopAdmin(models.Model):

    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=200,null=True)
    contact = models.CharField(max_length=30,null=True)


class Orders(models.Model):

    shop_id = models.ForeignKey(ShopAdmin, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):

    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(null=True)
    quantity_type=models.CharField(max_length=20, null=True)
