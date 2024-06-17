from django.urls import path

from .views import create_homework_view


urlpatterns = [
    path('', create_homework_view.create_homework, name='create_homework')
]
