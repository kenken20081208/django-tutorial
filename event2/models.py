from django.db import models


class Event2(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=200, null=True)

    # def __str__(self):
    #     return self.title
