from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),

    path('api/v1/classrooms/', include('apps.classroom.urls')),
    path('api/v1/teachers/', include('apps.teacher.urls')),
    path('api/v1/homeworks/', include('apps.homework.urls')),
    path('api/v1/assigned_homeworks/', include('apps.assigned_homework.urls')),

    path('admin/', admin.site.urls)
]
