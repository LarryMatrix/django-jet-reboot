from django.db import models


class RegionSampleModel(models.Model):
    payload_object = models.TextField()
    transaction_status = models.BooleanField(default=0)
    error_message = models.TextField()

    class Meta:
        pass

    def __str__(self):
        return '%d' %self.id

