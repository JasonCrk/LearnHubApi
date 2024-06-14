from django.urls import path

from apps.teacher.views import send_teacher_invitation_view


urlpatterns = [
    path('invitation/', send_teacher_invitation_view.send_invitation, name='send_teacer_invitation')
]
