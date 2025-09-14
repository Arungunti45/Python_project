from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)   # <-- no image here

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="product_images/", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Order(models.Model):
    PAYMENT_CHOICES = [
        ('UPI', 'UPI'),
        ('Card', 'Card'),
        ('COD', 'Cash on Delivery'),
    ]   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=20, blank=True, null=True)  # <-- add this
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order #{self.id} - {self.product.name}"