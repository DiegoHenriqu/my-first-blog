from django.db import models
from django.utils import timezone

class produto (models.,Model):
    sigla=models.CharField(max_length=1)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
         return self.title

class


