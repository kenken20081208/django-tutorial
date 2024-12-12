from django.db import models


class todo2(models.Model):
    title = models.CharField(max_length=200)
