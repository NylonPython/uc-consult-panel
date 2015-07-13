
from django.conf import settings
from django.db import models
# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Date Published')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post_content = models.TextField()
    def __unicode__(self):
        return self.post_title

class Location(models.Model):
    AFFILIATE = -1
    OPEN = 0
    CLASSROOM = 1
    LOCATION_TYPE_CHOICES = {
            (AFFILIATE, 'Affiliate Labs'),
            (OPEN, 'Open Labs'),
            (CLASSROOM, 'Classroom Labs')
    }
    lab_type = models.IntegerField(default=0, choices=LOCATION_TYPE_CHOICES)
    name = models.CharField(max_length = 100)
    building = models.CharField(max_length = 100)
    open_time = models.DateTimeField('Open Time')
    close_time = models.DateTimeField('Close Time')
    computer = models.ForeignKey('Computer')
    #printer = models.ForeignKey('Printer')
    printer_quantity = models.IntegerField()
    computer_quantity = models.IntegerField()

    def __unicode__(self):
        return self.name

class Computer(models.Model):
    computer_location = models.ForeignKey('Location', related_name='lab_computer')
    computer_model = models.ForeignKey('HardwareModel')
    computer_speed = models.IntegerField()
    computer_memory = models.IntegerField()
    computer_comment = models.CharField(max_length = 250, blank=True)
    def __unicode__(self):
        ret = self.computer_model.brand + ' ' + self.computer_model.model_num
        return ret
class Printer(models.Model):
    printer_location = models.ForeignKey('Location', related_name='lab_printers')
    printer_model = models.ForeignKey('HardwareModel')
    printer_comment = models.CharField(max_length = 250, blank=True)
    def __unicode__(self):
        ret = self.printer_model.brand + ' ' + self.printer_model.model_num
        return ret

class HardwareModel(models.Model):
    brand = models.CharField(max_length = 100)
    model_num = models.CharField(max_length = 30)
    def __unicode__(self):
        ret = self.brand + ' ' + self.model_num
        return ret
