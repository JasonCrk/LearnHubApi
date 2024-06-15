from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from ..models import Invitation
from ..serializers import InvitationCodesSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def accept_teacher_invitation(request: Request):
    invitation_serializer = InvitationCodesSerializer(data=request.data)

    if not invitation_serializer.is_valid():
        return Response({
            'validation_errors': invitation_serializer.errors
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    try:
        invitation = Invitation.objects.get(
            sub_code=invitation_serializer.data.sub_code,
            accept_code=invitation_serializer.data.accept_code)
    except Invitation.DoesNotExist:
        return Response({
            'message': 'The invitation does not exist'
        }, status=status.HTTP_404_NOT_FOUND)

    if invitation.user.pk != request.user.id:
        return Response({
            'message': 'The invitation is not for you'
        }, status=status.HTTP_400_BAD_REQUEST)

    classroom = invitation.teacher.class_room

    invitation.delete()

    classroom.teachers.add(request.user)

    return Response({
        'message': f'Invitation accepted! Welcome to the classroom {classroom.name}'
    })

