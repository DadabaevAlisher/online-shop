from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name="Foydalanuvchi")
    first_name = models.CharField(max_length=50, verbose_name="Ism")
    last_name = models.CharField(max_length=50, verbose_name="Familiya")
    phone = models.CharField(max_length=20, verbose_name="Telefon raqam")
    address = models.CharField(max_length=250, verbose_name="Manzil")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False, verbose_name="To'langanmi?")

    class Meta:
        ordering = ['-created']
        verbose_name_plural = "Buyurtmalar"
    
    def __str__(self):
        return f"Buyurtma #{self.id}"
    
    def get_total_cost(self):
        return sum(item.get.cost() for item in self.items.all())
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_items")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    quantity = models.PositiveBigIntegerField(default=1, verbose_name="Soni")

    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity
