from django.db import models


class todo(models.Model):
    title = models.CharField(max_length=200)