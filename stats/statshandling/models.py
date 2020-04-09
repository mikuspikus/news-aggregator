from django.db import models
from jsonfield import JSONField
from django.utils.translation import gettext_lazy as _


class GenericStat(models.Model):

    class Actions(models.TextChoices):
        PUT = 'PUT', _('PUT')
        POST = 'POST', _('POST')
        DELETE = 'DELETE', _('DELETE')
        PATCH = 'PATCH', _('PATCH')
        GET = 'GET', _('GET')

    user = models.UUIDField(null=True)
    datetimestamp = models.DateTimeField(auto_now=True)
    action = models.CharField(
        max_length=6,
        choices=Actions.choices,
        default=Actions.GET
    )
    input = JSONField(null=True, blank=True)
    output = JSONField(null=True, blank=True)

    class Meta:
        abstract = True
