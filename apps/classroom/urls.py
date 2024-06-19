from django.urls import path

from apps.classroom.views import (
    assign_teacher_as_classroom_owner_view,
    create_classroom_view,
    refresh_classroom_access_code_view,
    switch_activation_join_classroom_view,
    join_classroom_view
)


urlpatterns = [
    path(
        '',
        create_classroom_view.create_classroom,
        name='create_classroom'
    ),
    path(
        'join/<uuid:access_code>/',
        join_classroom_view.join_classroom,
        name='join_classroom'
    ),
    path(
        '<int:classroom_id>/join/activation/',
        switch_activation_join_classroom_view.switch_activation_join_classroom,
        name='switch_activation_join_classroom'
    ),
    path(
        '<int:classroom_id>/refresh-access/',
        refresh_classroom_access_code_view.refresh_classroom_access_code,
        name='refresh_classroom_access_code'
    ),
    path(
        '<int:classroom_id>/assign_owner/<int:teacher_id>/',
        assign_teacher_as_classroom_owner_view.assign_teacher_as_classroom_owner,
        name='assign_teacher_as_classroom_owner'
    )
]
