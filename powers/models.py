from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Power(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    speed = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(5)]
        )
    flight = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(5)]
        )
    strength = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(5)]
        )
    vision = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(5)]
        )
    fire = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(5)]
        )
    lasers = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(5)]
        )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content

# creates powers when a new account is made 
def create_power(sender, instance, created, **kwargs):
    if created:
        Power.objects.create(owner=instance)

post_save.connect(create_power, sender=User)