from django.contrib import admin
from uclabs import admin as uc_admin
from . import models
# Register your models here.


uc_admin.custom_admin.register(models.GroupStudyRoom)
uc_admin.custom_admin.register(models.GroupStudyRoomSchedule)
uc_admin.custom_admin.register(models.GroupStudyRoomReservation)
