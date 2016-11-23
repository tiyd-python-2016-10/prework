from django.db import models


class DTwit(models.Model):
    message = models.TextField(max_length=141)

    class Meta:
        ordering = ["-id"]
