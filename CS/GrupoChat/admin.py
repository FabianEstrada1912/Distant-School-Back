from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from GrupoChat.models import Chat

# Register your models here.

@admin.register(Chat)
class ChatAdmin (admin.ModelAdmin):
    list_display = ('pk', 'user','descripcion')
    list_display_links = ('pk', 'user',)
    list_editable_links = ('name','description')

    search_fields = (
        'descripcion',
        'user__username'
    )