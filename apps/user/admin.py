from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from apps.user.models import UserAccount

class UserAccountAdmin(BaseUserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'date_joined', 'is_admin']
    list_filter = ['is_admin']
    fieldsets = [
        (None, { 'fields': ['email', 'password'] }),
        ('Personal information', { 'fields': ['first_name', 'last_name', 'picture_url'] }),
        ('Persmissions', { 'fields': ['is_admin'] })
    ]
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = []

admin.site.register(UserAccount, UserAccountAdmin)
admin.site.unregister(Group)
