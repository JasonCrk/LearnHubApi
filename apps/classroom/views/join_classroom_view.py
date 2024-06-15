from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from apps.classroom.models import Classroom
from apps.student.models import Student

from uuid import UUID


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def join_classroom(request: Request, access_code: UUID):
    try:
        classroom = Classroom.objects.get(access_code=access_code)
    except Classroom.DoesNotExist:
        return Response({
            'message': 'The classroom does not exist'
        }, status=status.HTTP_404_NOT_FOUND)

    if not classroom.available_join:
        return Response({
            'message': 'The classroom does not allow more students'
        }, status=status.HTTP_400_BAD_REQUEST)

    student, created = Student.objects.get_or_create(
        user=request.user,
        classroom=classroom
    )

    if not created:
        if student.is_active:
            return Response({
                'message': 'You are already a student in this classroom'
            }, status=status.HTTP_400_BAD_REQUEST)

        student.is_active = True
        student.save()

    return Response({
        'message': 'Entered the classroom correctly'
    }, status=status.HTTP_200_OK)

