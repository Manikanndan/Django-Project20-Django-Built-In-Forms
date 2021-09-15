from app.models import Access_Record, Topic, Webpage
from django.contrib import admin

# Register your models here.
from app.models import *

class accessrecordscustomize(admin.ModelAdmin):
    list_display=['name','date']

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Access_Record,accessrecordscustomize)