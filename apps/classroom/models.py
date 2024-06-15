from django.db import models
from django.core.validators import MinLengthValidator

import uuid

from apps.user.models import UserAccount

from .validators import validate_hex_color


class Color(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=25,
        unique=True,
        validators=[MinLengthValidator(3)]
    )
    hex = models.CharField(
        max_length=7,
        unique=True,
        validators=[validate_hex_color]
    )

    def __str__(self) -> str:
        return self.name


class ClassroomManager(models.Manager):
    def create_classroom(self, user, **kwargs):
        return self.create(
            color=kwargs.get('color'),
            name=kwargs.get('name'),
            description=kwargs.get('description'),
            section=kwargs.get('section'),
            subject=kwargs.get('subject'),
            room=kwargs.get('room')
        ).teachers.add(user)


class Classroom(models.Model):
    banner_url = models.URLField(blank=True, null=True)
    picture_url = models.URLField(blank=True, null=True)
    available_join = models.BooleanField(default=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    name = models.CharField(
        verbose_name='Name',
        max_length=100,
        validators=[MinLengthValidator(3)]
    )
    access_code = models.UUIDField(
        verbose_name='Access code',
        default=uuid.uuid4,
        unique=True
    )
    description = models.TextField(
        verbose_name='Description',
        blank=True,
        null=True
    )
    section = models.CharField(
        verbose_name='Section',
        max_length=50,
        blank=True,
        null=True
    )
    subject = models.CharField(
        verbose_name='Subject',
        max_length=30,
        blank=True,
        null=True
    )
    room = models.CharField(
        verbose_name='Room',
        max_length=30,
        blank=True,
        null=True
    )
    teachers = models.ManyToManyField(
        UserAccount,
        through='teacher.Teacher',
        related_name='teachers'
    )
    students = models.ManyToManyField(
        UserAccount,
        through='student.Student',
        related_name='students'
    )

    objects = ClassroomManager()

    def __str__(self) -> str:
        return self.name

