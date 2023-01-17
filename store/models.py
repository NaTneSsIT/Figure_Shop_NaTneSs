from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True, blank=True)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
class Movie(models.Model):
    movie_name=models.CharField(max_length=200, null=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.movie_name

class Product(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, blank=True, null=True)
    prd_name = models.CharField(max_length=200, null=True)
    prd_price = models.FloatField()
    digital = models.BooleanField(default=True,null=True,blank=True)
    image=models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.prd_name
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=""
        return url
class product_Info(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    size = models.CharField(max_length=20,null=True)
    trademark=models.CharField(max_length=200,null=True)

class product_review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    score=models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    review=models.CharField(max_length=500,null=True)

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transacsion_id=models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        order_items=self.orderitem_set.all()
        total=sum([item.get_total for item in order_items])
        return total

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total
class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    create_at=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total=self.product.prd_price*self.quantity
        return total
class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address