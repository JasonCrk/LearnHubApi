import factory

from apps.teacher.models import Teacher

from __tests__.factories.classroom import ClassroomFactory
from __tests__.factories.user_account import UserAccountFactory


class TeacherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Teacher

    user = factory.SubFactory(UserAccountFactory)
    class_room = factory.SubFactory(ClassroomFactory)

class OwnerTeacherFactory(TeacherFactory):
    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return  manager.create_owner_teacher(*args, **kwargs)
