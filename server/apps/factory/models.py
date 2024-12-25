from django.db import models
from django.contrib.auth import get_user_model
from apps.production.models import AircraftModel, AircraftPart
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

User = get_user_model()
# Create your models here.
class AircraftModelFactory(models.Model):
    
    model_type = models.ForeignKey(AircraftModel, on_delete=models.CASCADE)
    made_by = models.ForeignKey(User, on_delete=models.CASCADE)
    made_at = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        ordering = ('made_at',)


class AircraftPartFactory(models.Model):

    part_type = models.ForeignKey(AircraftPart, on_delete=models.CASCADE)
    part_of = models.ForeignKey(AircraftModel, on_delete=models.CASCADE)
    made_by = models.ForeignKey(User, on_delete=models.CASCADE)
    made_at = models.DateTimeField(auto_now_add=True, null=False)
    # used_for = models.ForeignKey(AircraftModelFactory, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('made_at',)


@receiver(post_save, sender=AircraftPart, dispatch_uid="update_part_permissions")
def update_part_permissions(sender, instance, **kwargs):
    # TODO - Reverte item creation if any of the permissions creation fails
    Permission.objects.get_or_create(codename=f'can_add_{instance.name}', name=f'Can add {instance.name}', content_type=ContentType.objects.get_for_model(AircraftPartFactory))
    Permission.objects.get_or_create(codename=f'can_change_{instance.name}', name=f'Can change {instance.name}', content_type=ContentType.objects.get_for_model(AircraftPartFactory))
    Permission.objects.get_or_create(codename=f'can_delete_{instance.name}', name=f'Can delete {instance.name}', content_type=ContentType.objects.get_for_model(AircraftPartFactory))
    Permission.objects.get_or_create(codename=f'can_view_{instance.name}', name=f'Can view {instance.name}', content_type=ContentType.objects.get_for_model(AircraftPartFactory))
    
