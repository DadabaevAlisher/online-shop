from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos", verbose_name="Foydalanuvchi")
    title = models.CharField(max_length=150, verbose_name="Vazifa nomi")
    description = models.TextField(blank=True, verbose_name="Batafsil")
    completed =  models.BooleanField(default=False, verbose_name="Bajarildimi?")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
