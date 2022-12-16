from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Notes)
admin.site.register(Homework)
admin.site.register(Todo) #Register class Todo to admin.py

