from django.db import models
# To get access to the User database,
from django.contrib.auth.models import User

# Create your models here.
class Change(models.Model):
    equipment = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField('change date')
    implementer = models.ForeignKey(User)

    def __unicode__(self):
        output_width = 60
        pre_processed = self.date.strftime("%b %e, %Y at %H:%M") + ': ' + self.equipment + ': ' + self.description
        if len(pre_processed) > output_width:
            return pre_processed[:output_width] + '...'

        return pre_processed

class Problem(models.Model):
    description = models.CharField(max_length=1000)
    date = models.DateTimeField('discovered')
    caused_by = models.ManyToManyField(Change, related_name='caused_set', null=True, blank=True, default=None, limit_choices_to = {'date__lte': date.date})
    resolved_by = models.ManyToManyField(Change, related_name='resolved_set', null=True, blank=True, default=None, limit_choices_to = {'date__gte': date.date()})
    # ForeignKey.to_field
    # The field on the related object that the relation is to. By default, Django uses the primary key of the related object.

    def __unicode__(self):
        return self.date.strftime("%B %e, %Y at %H:%M") + ': ' + self.description

