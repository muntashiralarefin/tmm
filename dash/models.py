from django.db import models
# from django import forms
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _

# # Validator functions
# def validate_a2(value):
#     if value >99 or value < 10:
#         raise ValidationError(
#             _('Age should be 10 to 99'),
#             params={'value': value},
#         )


# # Create your models here.

# ## Main
# class tourist(models.Model):
#     a1_name = models.CharField('Tourist name',max_length=30)
#     a2_age = models.IntegerField('Age',  validators=[validate_a2])
#     a3_gender = models.CharField('Gender',max_length=30)
#     def __str__(self):
#         return self.a1_name
