from django.db import models

# Create your models here.
class CreateEvent(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title