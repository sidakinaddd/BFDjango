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
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True


class TopCategories(models.Manager):
    def get_queryset(self):
        return super(TopCategories, self).get_queryset().filter(status=True)


class NotTopCategories(models.Manager):
    def get_queryset(self):
        return super(NotTopCategories, self).get_queryset().filter(status=False)


class CategoryManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)


class Category(BasicInfo):
    # STATUS = (
    #     (1, 'top'),
    #     (2, 'not_top')
    # )
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    top_categories = TopCategories()
    not_top_categories = NotTopCategories()
    objects = CategoryManager()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class SoldOutProducts(models.Manager):
    def get_queryset(self):
        return super(SoldOutProducts, self).get_queryset().filter(status=1)


class InSellProducts(models.Manager):
    def get_queryset(self):
        return super(InSellProducts, self).get_queryset().filter(status=2)


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

    objects = ProductsManager()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
