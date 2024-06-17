from django.db import models


class Topic(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100, unique=True)
    classroom = models.ForeignKey('classroom.Classroom', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
