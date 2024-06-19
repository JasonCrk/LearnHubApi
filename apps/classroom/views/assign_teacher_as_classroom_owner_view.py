from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.classroom.models import Classroom
from apps.teacher.models import Teacher


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_teacher_as_classroom_owner(request: Request, classroom_id: int, teacher_id: int):
    try:
        classroom = Classroom.objects.get(pk=classroom_id)
    except Classroom.DoesNotExist:
        return Response({
            'message': 'The classroom does not exist'
        }, status=status.HTTP_404_NOT_FOUND)

    if not Teacher.objects.filter(user=request.user, classroom=classroom, owner=True):
        return Response({
            'message': 'You are not a teacher who owns this classroom'
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        teacher_to_owner = Teacher.objects.get(pk=teacher_id)
    except Teacher.DoesNotExist:
        return Response({
            'message': 'The teacher you want to designate as the classroom owner does not exist'
        }, status=status.HTTP_400_BAD_REQUEST)

    if teacher_to_owner.classroom_id != classroom.pk:
        return Response({
            'message': 'The teacher you want to designate as the classroom owner does not teach in this classroom'
        }, status=status.HTTP_400_BAD_REQUEST)

    teacher_to_owner.owner = True
    teacher_to_owner.save()

    return Response({
        'message': 'The teacher was assigned the owner of the classroom correctly'
    }, status=status.HTTP_200_OK)
