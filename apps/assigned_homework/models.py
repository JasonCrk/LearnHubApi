from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField

from apps.homework.models import Homework


class AssignedHomeworkStatus(models.TextChoices):
    PENDING = 'PEND', _('Pending')
    RESOLVED = 'RESOLV', _('Resolved')
    NO_RESOLVED = 'NORES', _('No resolved')


class AssignedHomework(models.Model):
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=6,
        choices=AssignedHomeworkStatus,
        default=AssignedHomeworkStatus.PENDING
    )
    grade = models.PositiveSmallIntegerField(
        null=True,
        blank=True
    )
    solution = ArrayField(
        models.URLField(),
        default=list,
        blank=True
    )
