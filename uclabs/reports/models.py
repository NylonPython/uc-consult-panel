from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from blog.models import Location
from django.utils import timezone
# Create your models here.



class Annotation(models.Model):
    POSITIVE = 1
    NEGATIVE = -1
    NEUTRAL = 0
    ANNOTATION_TYPE_CHOICES = {
            (POSITIVE,'Positive'),
            (NEGATIVE,'Negative'),
            (NEUTRAL,'Neutral')
    }
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name ='employee')
    supervisor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'supervisor')
    date = models.DateTimeField(default = timezone.now())
    ann_type = models.IntegerField('Annotation Type', default = NEGATIVE, choices = ANNOTATION_TYPE_CHOICES)
    ann_text = models.TextField('Annotation')
    def __unicode__(self):
        return 'Annotation for %s' % (self.employee)

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

class TroubleTicket(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL)
    location = models.ForeignKey('blog.Location')
    date = models.DateTimeField(default = timezone.now())
    machine_name = models.CharField('Machine Name', max_length=50)
    issue_description = models.TextField('Description', max_length=500)
    is_solved = models.BooleanField('Resolved', default = False)

class TimeSheetError(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL)
    location = models.ForeignKey('blog.Location')
    date = models.DateField(default = timezone.now())
    time_in = models.TimeField()
    time_out = models.TimeField()
    error_reason = models.TextField(max_length=150)

class PrintRefund(models.Model):
    BLACK_AND_WHITE = 0
    COLOR = 1
    PRINT_TYPE_CHOICES = {
        (BLACK_AND_WHITE,'Black and White'),
        (COLOR,'Color'),
    }

    employee = models.ForeignKey(settings.AUTH_USER_MODEL)
    user_m_number = models.CharField('M-Number (include M)', max_length = 9)
    location = models.ForeignKey('blog.Location')
    printer = models.ForeignKey('blog.Printer')
    num_pages = models.IntegerField()
    print_type = models.IntegerField('Type of Prints', default=BLACK_AND_WHITE, choices = PRINT_TYPE_CHOICES)
    refund_reason = models.TextField('Reason for Refund', default='Printing Error')
    is_refunded = models.BooleanField('Refunded', default=False)

class ProblemReport(models.Model):
    reporting_employee = models.ForeignKey(settings.AUTH_USER_MODEL)
    problem_date = models.DateTimeField()
    problem_type = models.TextField()