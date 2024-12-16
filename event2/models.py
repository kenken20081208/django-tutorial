from django.db import models


class Event2(models.Model):
    event2_text = models.CharField(max_length=200)
