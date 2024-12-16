from django.db import models


class Todo2(models.Model):
    title = models.CharField(max_length=200)
