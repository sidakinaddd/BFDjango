from django.core.management import BaseCommand
from onlineShop.models import Category


class Command(BaseCommand):
    help = "Number of sold  or in sell products"

    def add_arguments(self, parser):
        parser.add_argument('status', type=str, help='status of product')

    def handle(self, *args, **kwargs):
        status = kwargs['status']
        if status == 'sold':
             count= Category.objects.filter(status='1').count()
             self.stdout.write(self.style.SUCCESS(str(count)))
        elif status == 'insell':
            count = Category.objects.filter(status='2').count()
            self.stdout.write(self.style.SUCCESS(str(count)))
            self.stdout.write(self.style.SUCCESS('Top categories does not exist'))
