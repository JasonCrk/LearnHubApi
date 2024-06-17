from django.contrib.postgres.fields import ArrayField
from django.db import models

from apps.homework.validators import validate_datetime_is_future
from apps.topic.models import Topic


class Homework(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    teacher = models.ForeignKey('teacher.Teacher', on_delete=models.CASCADE)
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        null=True
    )
    deadline = models.DateTimeField(
        verbose_name='Deadline',
        validators=[validate_datetime_is_future]
    )
    classroom = models.ForeignKey(
        'classroom.Classroom',
        on_delete=models.CASCADE
    )
    resources = ArrayField(
        models.URLField(),
        default=list,
        blank=True
    )
