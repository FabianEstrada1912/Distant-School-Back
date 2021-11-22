
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from FriendUser.models import Friend

@admin.register(Friend)
class FriendUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user','idFriends')
    list_display_links = ('pk', 'user',)
    list_editable_links = ('user','created')

    search_fields = (
        'created',
        'user__username'
    )