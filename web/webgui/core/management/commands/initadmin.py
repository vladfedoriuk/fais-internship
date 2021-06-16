from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.conf import settings


class Command(BaseCommand):
    
    help = 'Creates a default admin.'
    
    def handle(self, *args, **options):
        try:
            superuser = User.objects.create_superuser(
                username=settings.DEFAULT_ADMIN.get('username'),
                password=settings.DEFAULT_ADMIN.get('password'),
                email=settings.DEFAULT_ADMIN.get('email'),
                is_staff=True,
                is_active=True,
                is_superuser=True
            )
            superuser.save()
        except:
            pass
        
