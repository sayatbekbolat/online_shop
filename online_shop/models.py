from django.db import models

class ProductType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Role(models.Model):
    SELLER = 1
    BUYER = 2
    ADMIN = 3

    ROLE_CHOICES = (
        (SELLER, 'seller'),
        (BUYER, 'buyer'),
        (ADMIN, 'admin')
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)
    
    def __str__(self):
        return self.get_id_display()

class User(models.Model):
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    roles = models.ManyToManyField(Role)

    def __str__(self):
        return self.email

class Product(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    sellers = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Basket(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField(default=0)

class Mini_Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField(default=0)
    basket = models.ForeignKey(Basket,on_delete=models.CASCADE)
    def __str__(self):
        return product


# Create your models here.
