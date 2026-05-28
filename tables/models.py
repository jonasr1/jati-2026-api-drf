from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    is_activate = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
