import factory

from apps.classroom.models import Classroom

from __tests__.factories.user_account import UserAccountFactory
from __tests__.factories.color import ColorFactory


class ClassroomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Classroom

    name = factory.Faker('pystr', max_chars=100, min_chars=3)
    color = factory.SubFactory(ColorFactory)


class ClassroomWithTeacherFactory(ClassroomFactory):

    user = factory.SubFactory(UserAccountFactory)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_classroom(*args, **kwargs)

