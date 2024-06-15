from django.urls import path

from apps.teacher.views import accept_teacher_invitation_view, send_teacher_invitation_view


urlpatterns = [
    path('invitation/', send_teacher_invitation_view.send_invitation, name='send_teacer_invitation'),
    path('invitation/accept/', accept_teacher_invitation_view.accept_teacher_invitation, name='accept_teacher_invitation')
]
