import getpass
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a Django admin user with default credentials'

    def handle(self, *args, **options):
        User = get_user_model()
        username = 'admin'
        email = 'admin@admin.com'
        password = 'asd123'

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR(f'User "{username}" already exists!'))
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully!'))
