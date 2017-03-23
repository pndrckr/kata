from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField(max_length=62)
    mobile = models.IntegerField
    street_address = models.CharField(max_length=95)
    post_code = models.CharField(max_length=10)
    city = models.CharField(max_length=35)
    country = models.CharField(max_length=70)
    nationality = models.CharField(max_length=70)
    photo = models.ImageField(upload_to="images", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title

