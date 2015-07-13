from django.contrib.admin import AdminSite
# Register your models here.

class ConsultAdminSite(AdminSite):
    site_header = 'UC Consultant Panel'
    site_title = 'UC Consultant Panel'
custom_admin = ConsultAdminSite()
