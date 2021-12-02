from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Conver.models import Cons
# Register your models here.
@admin.register(Cons)
class ConversacionAdmin (admin.ModelAdmin):
    list_display = ('pk', 'sender','receiver')
    list_display_links = ('pk', 'sender',)
    list_editable_links = ('sender','receiver')

    search_fields = (
        'sender',
        'receiver'
    )