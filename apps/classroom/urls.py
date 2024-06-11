from django.urls import path

from apps.classroom.views import create_classroom_view


urlpatterns = [
    path('', create_classroom_view, name='create_classroom')
]
