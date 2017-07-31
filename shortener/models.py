from django.db import models
import string
import random
from .utils import code_generator
# from code

# Create your models here.



class KirrURL(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        print('something')
        # self.shortcode = code_generator()
        super(KirrURL, self).save(*args,**kwargs)

    # def my_save(self):


    def __str__(self):
        return str(self.url)
