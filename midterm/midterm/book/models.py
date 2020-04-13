from django.db import models
import datetime
# Create your models here.
class BookJournalBase(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    description = models.TextField()
    created_date = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        abstract = True



class Book(BookJournalBase):
    num_pages = models.IntegerField(default=0)
    publisher = models.CharField(max_length=200)

    class Meta:
        permissions = (

        )

class Journal(BookJournalBase):
    TYPE = (
        ('Bullet', 'Bullet'),
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Sport', 'Sport'),
    )

    type = models.CharField(choices=TYPE,max_length=200)
    publisher = models.CharField(max_length=200)
