from django.contrib import admin

# Register your models here.
from.models import *
class LeadAdmin(admin.ModelAdmin):
    list_display=['name','email','phone_number','company','status','created_at']
admin.site.register(Lead,LeadAdmin)

class MapAdmin(admin.ModelAdmin):
    list_display=['db_field','csv_header']
admin.site.register(Mapping,MapAdmin)    