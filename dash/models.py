from django.db import models
# from django import forms
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _

# # Create your models here.

# ## Main
class Sex(models.Model):
    sex = models.CharField('Sex',max_length=30)
    def __str__(self):
        return self.asex

class Tourist(models.Model):
    a1_name = models.CharField('Tourist name',max_length=30)
    a2_age = models.IntegerField('Age')
    a3_gender = models.CharField('Gender',max_length=30)
    def __str__(self):
        return self.a1_name
