from rest_framework import serializers

from apps.assigned_homework.models import AssignedHomework, AssignedHomeworkStatus

from core.services.storage.azure.azure_storage import Storage


class CompleteAssignedHomeworkSerializer(serializers.ModelSerializer):
    solution_files = serializers.ListField(
        child=serializers.FileField(write_only=True),
        write_only=True,
        required=True,
        allow_empty=False
    )

    class Meta:
        model = AssignedHomework
        fields = [
            'solution_files'
        ]

    def validate_solution_files(self, value: list):
        for file in value:
            if file.size > 10 * 1024 * 1024:
                raise serializers.ValidationError(
                    "No file can be large than 10 megabytes"
                )

    def update(self, instance: AssignedHomework, validated_data):
        solution_files = validated_data.get('solution_files')
        solution: list[str] = []

        for file in solution_files:
            try:
                solution.append(Storage.upload_file(file).url)
            except:
                raise serializers.ValidationError(
                    "An error occurred while saving the selected files, please try again later"
                )

        instance.solution = solution
        instance.status = AssignedHomeworkStatus.RESOLVED
        instance.save()

        return instance
