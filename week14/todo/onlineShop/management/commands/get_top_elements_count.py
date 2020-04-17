from django.core.management import BaseCommand
from onlineShop.models import Category


class Command(BaseCommand):
    help = "Number of top elementsd"

    def add_arguments(self, parser):
        parser.add_argument('status', type=str, help='status of category')

    def handle(self, *args, **kwargs):
        status = kwargs['status']
        count= Category.objects.filter(status=status).count()
        if count>0:
            self.stdout.write(self.style.SUCCESS(str(count)))
        else:
            self.stdout.write(self.style.SUCCESS('Top categories does not exist'))
