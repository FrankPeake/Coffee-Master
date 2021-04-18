from django.contrib import admin
from django.contrib.auth.models import User
from .models import User, Profile, Beverage, Ingredient, Instruction, CustomBeverage, Feedback

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile,ProfileAdmin)

class BeverageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Beverage, BeverageAdmin)




