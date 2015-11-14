from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Investment(models.Model):
    company = models.CharField(max_length=30)
    market = models.CharField(max_length=20)
    option = models.CharField(max_length=5)
    price = models.CommaSeparatedIntegerField(max_length=6)
    volume = models.CommaSeparatedIntegerField(max_length=9)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
      return self.title
