from django.core.management.base import BaseCommand
from django.db.models import Avg, Max, Min, Sum
from onlineShop.models import Product, Category


class Command(BaseCommand):
    help = 'Get information about price'

    def handle(self, *args, **kwargs):
        data = [
            Product.objects.aggregate(Min('price')),
            Product.objects.aggregate(Sum('price')),
            Product.objects.aggregate(Avg('price')),
            Product.objects.aggregate(Max('price')),

        ]
        self.stdout.write(self.style.SUCCESS(data))