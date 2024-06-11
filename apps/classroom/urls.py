from django.urls import path

from apps.classroom.views import (
    create_classroom_view,
    join_classroom_view
)


urlpatterns = [
    path('', create_classroom_view.create_classroom, name='create_classroom'),
    path('join/<uuid:access_code>', join_classroom_view.join_classroom, name='join_classroom')
]
