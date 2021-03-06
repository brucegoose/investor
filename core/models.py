from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

VISIBILITY_CHOICES = (
(0, 'Public'),
(1, 'Anonymous'),
)

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
    visibility = models.IntegerField(choices=VISIBILITY_CHOICES, default=0)

    def __unicode__(self):
      return self.company

    def get_absolute_url(self):
      return reverse("investment_detail", args=[self.id])

class Analysis(models.Model):
  investment = models.ForeignKey(Investment)
  user = models.ForeignKey(User)
  create_at = models.DateTimeField(auto_now_add=True)
  text = models.TextField()
  visibility = models.IntegerField(choices=VISIBILITY_CHOICES, default=0)

  def __unicode__(self):
    return self.text

class Vote(models.Model):
  user = models.ForeignKey(User)
  investment = models.ForeignKey(Investment, blank=True, null=True)
  analysis = models.ForeignKey(Analysis, blank=True, null=True)

  def __unicode__(self):
    return "%s upvoted" % (self.suer.username)