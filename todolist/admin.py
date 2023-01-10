from django.contrib import admin
from . models import Task,Fileupload,Comment
admin.site.register(Task)
admin.site.register(Fileupload)
admin.site.register(Comment)
