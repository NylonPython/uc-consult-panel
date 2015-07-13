from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
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
    date = models.DateTimeField()
    ann_type = models.IntegerField('Annotation Type', default = NEGATIVE, choices = ANNOTATION_TYPE_CHOICES)
    ann_text = models.TextField('Annotation')
