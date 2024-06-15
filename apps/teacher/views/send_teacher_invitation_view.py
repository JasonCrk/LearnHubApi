from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from apps.student.models import Student
from apps.user.models import UserAccount

from ..mails import send_teacher_invitation
from ..models import Invitation, Teacher

import threading


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_invitation(request: Request):
    try:
        email = str(request.data.get('email'))
    except:
        return Response({
            'message': 'The email is required or invalid'
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    try:
        classroom_id = int(request.data.get('classroom_id'))
    except:
        return Response({
            'message': 'The email is required'
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    try:
        teacher = Teacher.objects.get(
            user=request.user,
            class_room__pk=classroom_id
        )
    except:
        return Response({
            'message': 'You are not a classroom teacher'
        }, status=status.HTTP_400_BAD_REQUEST)

    if not teacher.owner:
        return Response({
            'message': 'You don\'t own the classroom'
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = UserAccount.objects.get(email=email)
    except:
        return Response({
            'message': 'The user does not exist'
        }, status=status.HTTP_404_NOT_FOUND)

    if Teacher.objects.filter(user=user, class_room__pk=classroom_id).exists():
        return Response({
            'message': 'The user is already a teacher in the classroom'
        }, status=status.HTTP_400_BAD_REQUEST)

    if Student.objects.filter(
        user=user,
        class_room__pk=classroom_id,
        is_active=False
    ).exists():
        return Response({
            'message': 'The user is already a student in the classroom'
        }, status=status.HTTP_400_BAD_REQUEST)

    invitation = Invitation.create(teacher=teacher, user=user)

    threading\
        .Thread(
            target=send_teacher_invitation.send_teacher_mail,
            args=(
                email,
                request.user.email,
                request.user.get_full_name(),
                teacher.classroom.name,
                invitation.sub_code,
                invitation.accept_code
            )
        )\
        .start()

    return Response({
        'message': 'The invitation has been sent successfully'
    }, status=status.HTTP_200_OK)

