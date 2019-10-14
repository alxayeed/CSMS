#12345678
from django.contrib import admin
from .models import User,Order


# Register your models here.
admin.site.register(User)
admin.site.register(Order)