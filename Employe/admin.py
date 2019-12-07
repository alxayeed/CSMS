from django.contrib import admin
from .models import Area,Employe
from import_export.admin import ImportExportModelAdmin

class AreaAdmin(ImportExportModelAdmin
):
	list_display = ['area_code','area_name']
	list_filter = ['area_code','area_name']
	search_fields = ['area_code','area_name']

admin.site.register(Area,AreaAdmin)

class EmployeAdmin(ImportExportModelAdmin):
	list_display=['name','email','contact_no','work_area','address',]
	list_filter=['name','email','contact_no','work_area','address',]
	search_fields =['name','email','contact_no','work_area','address',]
admin.site.register(Employe,EmployeAdmin)

