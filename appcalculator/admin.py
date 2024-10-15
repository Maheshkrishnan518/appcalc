from django.contrib import admin

# Register your models here.
from  .models import Appcalculator,Feature

admin.site.register(Appcalculator)
admin.site.register(Feature)