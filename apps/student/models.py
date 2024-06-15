from django.db import models

from apps.classroom.models import Classroom
from apps.user.models import UserAccount


class Student(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.user.first_name
