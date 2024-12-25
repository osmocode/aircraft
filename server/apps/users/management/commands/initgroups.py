from django.core.management import BaseCommand, call_command
from django.contrib.auth.models import Group, Permission
from django.conf import settings
import json


class Command(BaseCommand):
    help = "Bypass django permissions id during fixture load"

    def handle(self, *args, **options):
        call_command('loaddata','default_groups.json')

        with open(settings.BASE_DIR / 'apps/users/fixtures/default_groups.json', 'r') as json_data:
            groups = json.load(json_data)
            for group in groups:
                g = Group.objects.get(pk=group['pk'])
                perms = list(map(lambda cd: Permission.objects.get(codename=cd), group['permissions']))
                g.permissions.set(perms)
                print(f'Installed {len(perms)} permission(s) for group: {g.name}')
            json_data.close()



