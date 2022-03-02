from operator import mod
from django.db import models

# Create your models here.
class Code(models.Model):
    code = models.CharField(max_length=2048)