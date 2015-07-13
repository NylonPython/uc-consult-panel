from django.contrib import admin
from .models import Headcount
# Register your models here.

class HeadcountAdmin(admin.ModelAdmin):
    list_display = ('date', 'location', 'employee', 'total_users', 'laptop_users', 'ss_users', 'group_users', 'gs_users' )

admin.site.register(Headcount, HeadcountAdmin)
