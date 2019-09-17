from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("title",)
