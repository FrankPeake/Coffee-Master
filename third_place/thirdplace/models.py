from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Removed couchbase support due to change in platform
#from django_couchbase import CBModel,CBNestedModel
#from django_couchbase import PartialReferenceField, ModelReferenceField
#from djangotoolbox.fields import ListField, EmbeddedModelField, DictField


# Create your models here.

## Models for User Objects
class User(models.Model):
    class Meta:
        abstract = True

    username = models.CharField(max_length=20, Null=False, Blank=False)
    password = models.CharField(max_length=20, Null=False, Blank=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=100, Unique=True, Blank=False, Null=False)
    city = models.CharField(max_length=50, Blank=False, Null=False)
    state_province = models.CharField(max_length=20, Blank=False, Null=False)

## Models for beverages

class Beverage(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=40)
    isCore = models.BinaryField(Null=False, Default=False)
    iced = models.BinaryField()
    type = models.CharField(max_length=15)
    ingredients = models.CharField()
    instructions = models.CharField()

class CustomBeverage(Beverage):
    class Meta:
        abstract = True    
    createdBy = models.ForeignKey(User,on_delete=CASCADE)

class Ingredient(models.Model):
    class Meta:
        abstract = True
    
    bevID = models.ForeignKey(Beverage,on_delete=CASCADE)
    ingName = models.CharField(max_length=5, Null=False, Blank=False)
    quantity = models.DecimalField(max_digits=3, decimal_places=1, Null=True, Blank=True)

class Instruction(models.Model):
    class Meta:
        abstract = True

    bevId = models.ForeignKey(Beverage,on_delete=CASCADE)
    instructionDetail = models.CharField(max_length=50)

class Feedback(models.Model):
    class Meta:
        abstract = True
    userID = models.ForeignKey(User,on_delete=CASCADE))
    beverageID = models.ForeignKey(Beverage,on_delete=CASCADE)
    rating = models.IntegerField(max_length=2, Null=True, Blank=True)
    comment = models.TextField())

