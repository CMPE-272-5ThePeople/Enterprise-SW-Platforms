# Create your models here.
from django.db import models


# Create your models here.
class Notifications(models.Model):
    message = models.CharField(max_length=999)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.message
