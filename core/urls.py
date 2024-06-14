from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),

    path('api/v1/classrooms/', include('apps.classroom.urls')),
    path('api/v1/teachers/', include('apps.teacher.urls')),

    path('admin/', admin.site.urls)
]
