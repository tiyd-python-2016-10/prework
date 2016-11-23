from django.db import models


# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length=32)


class Task(models.Model):
    status = models.ForeignKey(Status)
    task = models.TextField()

    def __str__(self):
        return self.task
