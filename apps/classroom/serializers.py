from rest_framework.schemas.coreapi import serializers
from rest_framework.serializers import ModelSerializer

from apps.classroom.models import ClassRoom, Color


class CreateClassroomSerializer(ModelSerializer):
    color_id = serializers.IntegerField(min_value=1)

    class Meta:
        model = ClassRoom
        fields = [
            'name',
            'color_id',
            'description',
            'section',
            'subject',
            'room'
        ]

    def validate_color_id(self, value: int):
        if not Color.objects.filter(pk=value).exists():
            return serializers.ValidationError('The color does not exist')

    def create(self, validated_data):
        color = Color.objects.get(pk=validated_data['color_id'])
        return ClassRoom(**validated_data, color=color)

