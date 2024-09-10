from django import forms
from .models import Products, ShopAdmin, Orders, OrderItem

class Add_ShopForm(forms.ModelForm):

    class Meta:
        model = ShopAdmin
        fields = ['name','description','address','contact']


class Add_ProductsForm(forms.ModelForm):

    class Meta:
        model=Products
        fields = ['code', 'name','description','type','brand','category','price','stock','product_color']

class Create_Order(forms.ModelForm):

    class Meta:
        models=Orders
        fields=['shop_id']

class Add_OrderItem(forms.ModelForm):

    class Meta:
        model=OrderItem
        fields=['product', 'quantity','quantityType']