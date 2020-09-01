from django.db import models
from usersapp.models import Users

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

class Post(models.Model):
    writer=models.ForeignKey(Users,on_delete=models.CASCADE)
    title=models.TextField()
    content=models.TextField()
    writedate=models.DateTimeField(auto_now_add=True)
    cnt=models.IntegerField(default=0)
    like=models.IntegerField(default=0)

    @property
    def update_counter(self):
        self.cnt+=1
        self.save()

    @property
    def up_like(self):
        self.like+=1
        self.save()

    @property
    def down_like(self):
        self.like-=1
        self.save()

class recommend(models.Model):
    useremail=models.ForeignKey(Users,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
