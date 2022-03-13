from email.policy import default
from django.db import models


# Create your models here.


class CharactorData(models.Model):
	name = models.CharField(max_length=30, null=True)
	force = models.TextField(max_length=300, null=True)

def __str__(self):
    return self.name
















