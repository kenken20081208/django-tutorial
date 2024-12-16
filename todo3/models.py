from django.db import models


class todo3(models.Model):
    title = models.CharField(max_length=200)
