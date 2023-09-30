from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length = 180)
    location = models.CharField(max_length = 180)
    phone = models.CharField(max_length = 180)
    target = models.IntegerField()
    pembejeo_type = models.CharField(max_length = 180, blank=True)
    pembejeo_desc = models.CharField(max_length = 180, blank=True)
    ushauri_desc = models.TextField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
