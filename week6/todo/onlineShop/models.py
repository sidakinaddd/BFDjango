from django.db import models

# Create your models here.
from django.db import models
from auth_.models import MyUser

class CategoryManager(models.Manager):
    def for_user(self,user):
        return self.filter(owner=user)

class Category(models.Model):
    name= models.CharField(max_length=100)
    owner=models.ForeignKey(MyUser, on_delete=models.CASCADE)
    objects= CategoryManager()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'Product'
        verbose_name = 'Products'