from auth_.models import MyUser
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from onlineShop.models import Category, Product

class Command(BaseCommand):
    help = 'Creating new category'

    def add_arguments(self, parser):
        parser.add_argument('-o','--owner', type=str, help="Name of owner")
        parser.add_argument('-n','--name', type=str, help='Name of name))')
        parser.add_argument('-d', '--description', type=str, help='description text')

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE('In process'))
        owner_name = kwargs['owner']
        owner = MyUser.objects.get(first_name=owner_name)
        name = kwargs['name']
        description = kwargs['description']
        if Category.objects.create(name=name, owner=owner,description=description):
            self.stdout.write(self.style.SUCCESS('Category is created'))
        else:
            self.stdout.write(self.style.ERROR('Got some problems'))





