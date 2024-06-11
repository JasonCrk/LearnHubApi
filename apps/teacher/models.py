from django.db import models

from apps.classroom.models import ClassRoom
from apps.user.models import UserAccount


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

