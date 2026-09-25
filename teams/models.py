from django.db import models
from django.conf import settings
# Create your models here.

class Team(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through="TeamMembership", related_name='teams')
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class TeamMembership(models.Model):

    ROLES_CHOICES = [
        ('manager', 'Team Manager'),
        ('member', 'Team Member')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLES_CHOICES)
    date_added = models.DateField(auto_now_add=True)