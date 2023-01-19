from django.db import models
from time import *

# Create your models here.
class chat(models.Model):
    my = models.CharField(max_length=1000)
    res = models.CharField(max_length=1000)

    def __str__(self):
        return strftime('%I : %M : %S %p')