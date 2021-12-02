from django.contrib import admin
from django.contrib.auth.models import User
from GrupoChat.models import Chat
from ListaChat.models import ListChat

@admin.register(ListChat)
class ListChantAdmi(admin.ModelAdmin):
    list_display = ('pk', 'user','chat')
    list_display_links = ('pk', 'user',)
    list_editable_links = ('user','chat')

    search_fields = (
        'chat',
        'user__username'
    )