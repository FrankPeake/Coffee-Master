from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Removed couchbase support due to change in platform
#from django_couchbase import CBModel,CBNestedModel
#from django_couchbase import PartialReferenceField, ModelReferenceField
#from djangotoolbox.fields import ListField, EmbeddedModelField, DictField


# Create your models here.

## Models for User Objects
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    city = models.CharField(max_length=50, null=False,blank=False)
    state_province = models.CharField(max_length=20, null=False,blank=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

## Models for beverages



class Beverage(models.Model):
    

    name = models.CharField(max_length=40)
    isCore = models.BinaryField(null=False, default=False)
    iced = models.BinaryField()
    type = models.CharField(max_length=15)


class Ingredient(models.Model):
    
    bevID = models.ForeignKey(Beverage,on_delete=CASCADE)
    ingName = models.CharField(max_length=5, null=False, blank=False)
    quantity = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

class Instruction(models.Model):


    bevID = models.ForeignKey(Beverage, on_delete=CASCADE)
    instructionDetail = models.CharField(max_length=50)

class CustomBeverage(Beverage):
     
    createdBy = models.ForeignKey(User,on_delete=CASCADE)



class Feedback(models.Model):

    userID = models.ForeignKey(User,on_delete=CASCADE)
    beverageID = models.ForeignKey(Beverage,on_delete=CASCADE)
    rating = models.IntegerField(null=True, blank=True)
    comment = models.TextField()

