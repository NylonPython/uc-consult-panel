from django.db import models
from django.conf import settings
from blog.models import Location
from django.utils import timezone
# Create your models here.

class Headcount(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL)
    date = models.DateTimeField(default = timezone.now())
    location = models.ForeignKey('blog.Location')
    total_users = models.IntegerField('Total Users')
    laptop_users = models.IntegerField('Laptop Users')
    ss_users = models.IntegerField('Silent Study Ussers')
    group_users = models.IntegerField('Users in Groups')
    gs_users = models.IntegerField('Users in Group Study Room')
    class Meta:
        permissions = (("can_view_headcounts", "Can View Headcount"),)
