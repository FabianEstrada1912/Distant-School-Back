from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from Profile.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user','description')
    list_display_links = ('pk', 'user',)
    list_editable_links = ('name','description')

    search_fields = (
        'description',
        'user__username'
    )