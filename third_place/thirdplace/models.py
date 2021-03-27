from django import models
from django_couchbase import CBModel,CBNestedModel
from django_couchbase import PartialReferenceField, ModelReferenceField
from djangotoolbox.fields import ListField, EmbeddedModelField, DictField


# Create your models here.

class Ingredient(CBModel):
    class Meta:
        abstract = True
    
    doc_type = 'ingredient'
    id_prefix = 'igr'

    cupID = models.charField(max_length=5, null=False, blank=False)
    name = models.charField(max_length=30, null=False, blank=False)
    ingType = models.charField(max_length=10)
    quantity = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)

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
    isCore = models.Binary_Field(null=False, Default=False)
    iced = models.Binary_Field()
    type = models.CharField(max_length=15)
    ingredients = ListField(EmbeddedModelField(Ingredient))
    instructions = ListField(EmbeddedModelField(Instruction))





    

