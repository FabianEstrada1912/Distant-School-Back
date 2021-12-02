from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Conversacion.models import Conversacion
# Register your models here.
@admin.register(Conversacion)
class ConversacionAdmin (admin.ModelAdmin):
    list_display = ('pk', 'sender','receiver')
    list_display_links = ('pk', 'sender',)
    list_editable_links = ('sender','receiver')

    search_fields = (
        'sender',
        'receiver'
    )