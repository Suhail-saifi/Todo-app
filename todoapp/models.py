from django.db import models

# Create your models here.
class Mytodo(models.Model):
    task = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.task