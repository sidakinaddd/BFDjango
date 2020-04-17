from django.db import models

# Create your models here.
from django.db import models
from auth_.models import MyUser
from django.db.models import signals



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
    image = models.ImageField(upload_to='images', null=True)
    attachment = models.FileField(upload_to='attachments', null=True)

    top_categories = TopCategories()
    not_top_categories = NotTopCategories()
    objects = CategoryManager()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    @property
    def information(self):
        return self.name + ' ' + self.description

    @classmethod
    def get_count_of_top(cls):
        return cls.top_categories.count()

    @classmethod
    def get_count_of_not_top(cls):
        return cls.not_top_categories.count()


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
    price = models.FloatField(default=0)
    status = models.IntegerField(choices=STATUS, default=2)

    sold_out_products = SoldOutProducts()
    in_sell_products = InSellProducts()

    objects = ProductsManager()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    #  discount
    @property
    def get_with_discount(self):
        return self.price-10

    @classmethod
    def get_sold_out_products_count(cls):
        return cls.sold_out_products.count()

    @classmethod
    def get_in_sell_products_count(cls):
        return cls.in_sell_products.count()


# b = Category()
# b.get_count_of_top()
