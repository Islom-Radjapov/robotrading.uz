from django.db import models


class Database(models.Model):
    login = models.CharField(max_length=120)
    date = models.DateTimeField()
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)


    def __str__(self):
        return self.name