from django.core.management import BaseCommand, call_command
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Bypass django password hash during fixture load"

    def handle(self, *args, **options):
        call_command('loaddata','default_users.json')
        # Fix the passwords of fixtures
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()