from django.db import models


class event(models.Model):
    event_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
