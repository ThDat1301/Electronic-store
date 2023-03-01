from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='home_page/images/collection', default=None)

    def countProduct(self):
        num = Product.objects.filter(category=self).all().count()
        return num

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='products/%Y/%m', default=None)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category,related_name='category', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m', default=None)

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField(blank=True)
    product = models.ForeignKey(Product, related_name='comment', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)


class Order(models.Model):
    orderDate = models.DateField(auto_now_add=True)
    orderStatus = models.BooleanField(default=False)
    orderAddress = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE)


class OrderDetail(models.Model):
    price = models.FloatField()
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(Product, related_name='order_detail', on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, related_name='order_detail', on_delete=models.DO_NOTHING)

