#12345678
from django.contrib import admin
from .models import User,Order
from import_export.admin import ImportExportModelAdmin



# Register your models here.
class UserAdmin(ImportExportModelAdmin):
	list_display=[field.name for field in User._meta.get_fields()]
	list_filter=('first_name','email','contact_no','address')
	search_fields = ('first_name','last_name','email','contact_no','address')

	# readonly_fields = [field.name for field in User._meta.get_fields()]
	# # filter_horizontal=
	# # fieldsets = 



admin.site.register(User,UserAdmin)

class OrderAdmin(ImportExportModelAdmin):
	list_display=('order_id','sender_name','sender_email','reciever_name','reciever_email','product_name','status')
	list_filter=('sender_name','sender_email','reciever_name','reciever_email','product_name','status')
	# search_fields = ('order_id','sender_name','order_area')
	readonly_fields = [field.name for field in Order._meta.get_fields()]

admin.site.register(Order,OrderAdmin)
