from django.db import models
from teams.models import Team
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=20)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL, related_name='projects')

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=20)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')