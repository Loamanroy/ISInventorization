from django.db import models


class Catalog(models.Model):
    title = models.TextField(max_length=255)
    imageItem = models.ImageField()
    countItem = models.IntegerField()
    depart = models.ForeignKey('Departments', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Departments(models.Model):
    name = models.TextField(max_length=255, null=True)

    def __str__(self):
        return self.name
