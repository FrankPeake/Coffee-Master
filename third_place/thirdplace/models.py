from django import models
from django_couchbase import CBModel,CBNestedModel
from django_couchbase import PartialReferenceField, ModelReferenceField
from djangotoolbox.fields import ListField, EmbeddedModelField, DictField


# Create your models here.


## Models for beverages
class Ingredient(CBModel):
    class Meta:
        abstract = True
    
    doc_type = 'ingredient'
    id_prefix = 'igr'

    cupID = models.charField(max_length=5, Null=False, Blank=False)
    name = models.charField(max_length=30, Null=False, Blank=False)
    ingType = models.charField(max_length=10)
    quantity = models.DecimalField(max_digits=3, decimal_places=1, Null=True, Blank=True)

class Instruction(CBNestedModel):
    class Meta:
        abstract = True

    doc_type = 'instruction'
    id_prefix = 'ins'

    instructionDetail = models.CharField(max_length=50)

class Beverage(CBModel):
    class Meta:
        abstract = True

    doc_type = 'beverage'
    id_prefix = 'bev'

    name = models.charField(max_length=40)
    isCore = models.Binary_Field(Null=False, Default=False)
    iced = models.Binary_Field()
    type = models.CharField(max_length=15)
    ingredients = ListField(EmbeddedModelField(Ingredient))
    instructions = ListField(EmbeddedModelField(Instruction))

## Models for User Objects

class Feedback(CBNestedModel):
    class Meta:
        abstract = True

    doc_type = 'feedback'
    id_prefix = 'fb'

    rating = models.IntegerField(max_length=2, Null=True, Blank=True)
    comment = models.TextField()

class User(CBModel):
    class Meta:
        abstract = True
    
    doc_type = 'user'
    id_prefix = 'usr'

    username = models.CharField(max_length=20, Null=False, Blank=False)
    password = models.CharField(max_length=20, Null=False, Blank=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=100, Unique=True, Blank=False, Null=False)
    city = models.CharField(max_length=50, Blank=False, Null=False)
    state_province = models.CharField(max_length=20, Blank=False, Null=False)
    feedback = ListField(EmbeddedModelField(Feedback))



    

