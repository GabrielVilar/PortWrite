from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_writer', 'is_moderator', 'is_administrator')
    list_filter = ('is_writer', 'is_moderator', 'is_administrator')
    search_fields = ('username', 'email')
    actions = ['make_writer']

    def make_writer(self, request, queryset):
        queryset.update(is_writer=True)
    make_writer.short_description = "Grant writer status to selected users"

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
