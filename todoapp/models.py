from django.contrib.auth.models import User
from django.db import models

class Mytodo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task = models.CharField(max_length=255)
    # Add other fields as necessary

    def __str__(self):
        return self.task
