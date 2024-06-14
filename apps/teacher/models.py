from django.db import models

from apps.classroom.models import ClassRoom
from apps.user.models import UserAccount

from .fields import generate_code

import uuid


class TeacherManager(models.Manager):
    def create_owner_teacher(self, user, classroom):
        return self.create(user=user, class_room=classroom, owner=True)


class Teacher(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    owner = models.BooleanField(default=False)

    objects = TeacherManager()

    def __str__(self) -> str:
        return self.user.firt_name


class Invitation(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    sub_code = models.CharField(
        verbose_name='Sub code',
        max_length=9,
        default=generate_code,
        unique=True
    )
    accept_code = models.UUIDField(
        verbose_name='Accept code',
        default=uuid.uuid4,
        unique=True
    )

