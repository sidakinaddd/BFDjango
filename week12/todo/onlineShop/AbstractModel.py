from django.db import models
class BaseProduct(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    existance = models.BooleanField()

    class Meta:
        abstract = True

class OnlineProduct(BaseProduct):
    status = models.CharField()


class OfflineProduct(BaseProduct):
    address = models.CharField()
