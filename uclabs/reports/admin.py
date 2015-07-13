from django.contrib import admin
from uclabs import admin as uc_admin
from . import models
# Register your models here.

class HeadcountAdmin(admin.ModelAdmin):
    list_display = ('date', 'location', 'employee', 'total_users', 'laptop_users', 'ss_users', 'group_users', 'gs_users' )

uc_admin.custom_admin.register(models.Headcount, HeadcountAdmin)

class AnnotationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'supervisor', 'ann_type', 'ann_text')

uc_admin.custom_admin.register(models.Annotation, AnnotationAdmin)

class TroubleTicketAdmin(admin.ModelAdmin):
	list_display = ('employee', 'machine_name', 'location', 'date', 'issue_description', 'is_solved')

uc_admin.custom_admin.register(models.TroubleTicket, TroubleTicketAdmin)

class TimeSheetErrorAdmin(admin.ModelAdmin):
	list_display = ('employee', 'location', 'date', 'time_in', 'time_out', 'error_reason')

uc_admin.custom_admin.register(models.TimeSheetError, TimeSheetErrorAdmin)

class PrintRefundAdmin(admin.ModelAdmin):
	list_display = ('employee', 'user_m_number', 'location', 'printer', 'num_pages', 'print_type', 'refund_reason', 'is_refunded')

uc_admin.custom_admin.register(models.PrintRefund, PrintRefundAdmin)

class ProblemReportAdmin(admin.ModelAdmin):
	list_display = ('reporting_employee', 'problem_date', 'problem_type')

uc_admin.custom_admin.register(models.ProblemReport, ProblemReportAdmin)
