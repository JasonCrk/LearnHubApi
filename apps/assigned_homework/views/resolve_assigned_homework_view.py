from django.db import transaction

from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.assigned_homework.serializers import CompleteAssignedHomeworkSerializer

from ..models import AssignedHomework, AssignedHomeworkStatus


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@transaction.atomic
def resolve_assigned_homework(request: Request, assigned_homework_id: int):
    try:
        assigned_homework = AssignedHomework.objects.get(pk=assigned_homework_id)
    except AssignedHomework.DoesNotExist:
        return Response({
            'message': 'The assigned homework does not exist'
        }, status=status.HTTP_404_NOT_FOUND)

    complete_assigned_homework = CompleteAssignedHomeworkSerializer(
        assigned_homework,
        data={'solution_files': request.data.dict().get('solution')},
        partial=True
    )

    if not complete_assigned_homework.is_valid():
        return Response({
            'validation_errors': complete_assigned_homework.errors
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    if assigned_homework.student.user_id != request.user.id:
        return Response({
            'message': 'The homework is not for you'
        }, status=status.HTTP_400_BAD_REQUEST)

    if assigned_homework.status != AssignedHomeworkStatus.PENDING:
        return Response({
            'message': 'The task has been completed or its deadline has expired'
        }, status=status.HTTP_400_BAD_REQUEST)

    complete_assigned_homework.save()

    return Response({
        'message': 'The solution to the task was delivered successfully'
    }, status=status.HTTP_200_OK)
