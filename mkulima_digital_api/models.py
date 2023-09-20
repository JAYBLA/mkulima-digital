from django.db import models


class Pembejeo(models.Model):
    name = models.CharField(max_length = 180)    
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Target(models.Model):
    name = models.CharField(max_length = 180)    
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Feedback(models.Model):
    name = models.CharField(max_length = 180)
    location = models.CharField(max_length = 180)
    phone = models.CharField(max_length = 180)
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    pembejeo = models.ForeignKey(Pembejeo, on_delete=models.CASCADE, blank = True, null=True)
    description = models.TextField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
