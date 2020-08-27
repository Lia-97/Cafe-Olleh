from django.db import models

# Create your models here

class Product(models.Model):
    id=models.IntegerField(primary_key=True)
    products=models.CharField(max_length=20)

class Product_Bybrand(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE,primary_key=True)
    Starbucks=models.CharField(max_length=30, null=True)
    Twosome=models.CharField(max_length=30, null=True)
    TomandToms=models.CharField(max_length=30, null=True)
    Ediya=models.CharField(max_length=30, null=True)
    Mega=models.CharField(max_length=30, null=True)
    Hollys=models.CharField(max_length=30, null=True)
    Coffeebean=models.CharField(max_length=30, null=True)
    Coffeebay=models.CharField(max_length=30, null=True)
    Angelinus=models.CharField(max_length=30, null=True)
    Pascucci=models.CharField(max_length=30, null=True)

class Price_Bybrand(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE,primary_key=True)
    Starbucks=models.IntegerField(null=True)
    Twosome=models.IntegerField(null=True)
    TomandToms=models.IntegerField(null=True)
    Ediya=models.IntegerField(null=True)
    Mega=models.IntegerField(null=True)
    Hollys=models.IntegerField(null=True)
    Coffeebean=models.IntegerField(null=True)
    Coffeebay=models.IntegerField(null=True)
    Angelinus=models.IntegerField(null=True)
    Pascucci=models.IntegerField(null=True)

class Brand(models.Model):
    id=models.IntegerField(primary_key=True)
    brand=models.CharField(max_length=15)

class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    store=models.CharField(max_length=30)
    location=models.CharField(max_length=50)
    lat=models.FloatField(null=True)
    lng=models.FloatField(null=True)