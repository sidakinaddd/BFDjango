from django.db import models

# importing the sys module

# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs

# Create your models here.
from django.db import models
from auth_.models import MyUser


class BasicInfo(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        abstract = True


class CategoryManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)


class Category(BasicInfo):
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    objects = CategoryManager()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class SoldOutProducts(models.Manager):
    def get_queryset(self):
        return self.filter(status=1)


class InSellProducts(models.Manager):
    def get_queryset(self):
        return self.filter(status=2)

class ProductsManager(models.Manager):
    pass


class Product(BasicInfo):
    STATUS = (
        (1, 'sold_out'),
        (2, 'in_sell')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=2)

    sold_out_products = SoldOutProducts()
    in_sell_products = InSellProducts()

    objects=ProductsManager()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        # unique_together = ('category','name')
        # ordering = ('price',)
# #классовый метод
#     @classmethod
#     def top_ten(cls):
#         return cls.objects.all()[:10]
# #instance method b.price_round()
#     @property
#     def price_round(self):
#         return round(self.price, 3)
#     #print(p.price_round())
#     def __str__(self):
#         return self.name
