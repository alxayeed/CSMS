from django.contrib import admin
from .models import Area,Employe


# class RatingAdmin(admin.ModelAdmin):
#     readonly_fields = ('date')


# # Register your models here.
# admin.site.register(Rating,RatingAdmin)
admin.site.register(Area)
admin.site.register(Employe)

