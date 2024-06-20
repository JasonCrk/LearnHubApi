from django.urls import path

from apps.assigned_homework.views import (
    resolve_assigned_homework_view
)

urlpatterns = [
    path(
        '<int:assigned_homework_id>/resolve/',
        resolve_assigned_homework_view.resolve_assigned_homework,
        name='resolve_assigned_homework'
    )
]
