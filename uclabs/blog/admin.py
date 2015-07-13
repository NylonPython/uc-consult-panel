from django.contrib import admin
from uclabs import admin as uc_admin
from .models import Location, Post, Computer, Printer, HardwareModel
# Register your models here.

uc_admin.custom_admin.register(Post)
uc_admin.custom_admin.register(Location)
uc_admin.custom_admin.register(Computer)
uc_admin.custom_admin.register(Printer)
uc_admin.custom_admin.register(HardwareModel)
