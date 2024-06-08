from django.db import models


class Topic(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100, unique=True)

    def __str__(self):
        return self.name
