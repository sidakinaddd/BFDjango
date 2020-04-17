from django.core.management import BaseCommand

from onlineShop.models import Product

class Command(BaseCommand):
    help = "Delete all products"

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('All products are going to be deleted'))
        if Product.objects.all().count() == 0:
            self.stdout.write(self.style.SUCCESS('There are no products'))
        else:
            Product.objects.all()
            self.stdout.write(self.style.SUCCESS('Products are deleted!'))
