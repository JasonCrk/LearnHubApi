from django.db import transaction

from rest_framework import serializers

from apps.homework.models import Homework
from apps.student.models import Student
from apps.assigned_homework.models import AssignedHomework

from core.services.storage.azure.azure_storage import Storage

from datetime import datetime


class CreateHomeworkSerializer(serializers.ModelSerializer):
    resources_files = serializers.ListField(
        child=serializers.FileField(write_only=True),
        write_only=True,
        required=False
    )
    students = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(),
        many=True,
        write_only=True,
        required=True
    )

    class Meta:
        model = Homework
        fields = [
            'name',
            'topic',
            'teacher',
            'description',
            'deadline',
            'classroom',
            'students',
            'resources_files'
        ]

    def validate_resources_files(self, value: list):
        for file in value:
            if file.size > 10 * 1024 * 1024:
                raise serializers.ValidationError(
                    "No file can be large than 10 megabytes"
                )

    def validate_deadline(self, value: datetime):
        if datetime.now() < value:
            raise serializers.ValidationError(
                "Must be greater than the current date"
            )

    def validate(self, attrs):
        teacher = attrs['teacher']
        classroom = attrs['classroom']

        if teacher.classroom_id != classroom.id:
            raise serializers.ValidationError(
                "The teacher does not teach in the classroom"
            )

        for student in attrs['students']:
            if student.classroom_id != classroom:
                raise serializers.ValidationError(
                    'Students must belong to the same classroom'
                )

    def create(self, validated_data):
        resources = []
        resources_files = validated_data.pop('resources_files', [])
        students = validated_data.pop('students', [])

        with transaction.atomic():
            for file in resources_files:
                try:
                    file_url = Storage.upload_file(file).url
                    resources.append(file_url)
                except:
                    raise serializers.ValidationError(
                        "An error occurred while saving the selected files, please try again later"
                    )

            homework = Homework.objects.create(**validated_data, resources=resources)

            for student in students:
                AssignedHomework.objects.create(
                    student=student,
                    homework=homework
                )

            return homework
