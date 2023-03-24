from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    link = models.CharField(max_length=64)
    pdf = models.FileField()
    def __str__(self):
        return f"{self.title} | {self.author}"