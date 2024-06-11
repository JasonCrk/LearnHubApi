import factory

from apps.classroom.models import Color


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Color

    name = factory.Faker('name')
    hex = factory.Faker('hex_color')
