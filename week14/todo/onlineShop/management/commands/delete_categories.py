from django.core.management import BaseCommand
from onlineShop.models import Category


class Command(BaseCommand):
    help = "Category is going to be deleted"

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='id og category')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        if Category.objects.get(id=id):
            Category.objects.get(id=id).delete()
            self.stdout.write(self.style.SUCCESS('Category is deleted'))
        else:
            self.stdout.write(self.style.SUCCESS('Category does not exist'))
