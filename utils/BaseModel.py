from django.db import models
from django.conf import settings


class DateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False,null=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.PROTECT, related_name='%(class)s_requests_created')
    update_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.PROTECT, related_name='%(class)s_requests_updated')

    class Meta:
        abstract = True