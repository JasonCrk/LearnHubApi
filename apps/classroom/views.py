from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import Request, Response, status
from rest_framework.permissions import IsAuthenticated

from apps.classroom.serializers import CreateClassroomSerializer
from apps.teacher.models import Teacher


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_classroom_view(request: Request):
    classroom_data = request.data

    new_classroom_serializer = CreateClassroomSerializer(data=classroom_data)

    if not new_classroom_serializer.is_valid():
        return Response(
            {'validation_errors': new_classroom_serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    new_classroom = new_classroom_serializer.save()

    Teacher.objects.create_owner_teacher(user=request.user, classroom=new_classroom)

    return Response(
        {'message': 'The classroom was created successful'},
        status=status.HTTP_201_CREATED
    )

