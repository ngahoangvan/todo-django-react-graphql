from django.db import models
from ..users.models import UserProfile


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    date = models.CharField(max_length=100)
    created_by = models.ForeignKey(
        UserProfile,
        related_name='events',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("title",)
