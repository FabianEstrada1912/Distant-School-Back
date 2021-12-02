from django.db import models
from django.contrib.auth.models import User
from GrupoChat.models import Chat


class ListChat(models.Model):
    user =  models.ForeignKey(User,blank=True, null=True,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    chat = models.ForeignKey(Chat, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "ListChat"