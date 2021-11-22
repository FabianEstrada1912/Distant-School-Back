from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Friend(models.Model):
    user =  models.ForeignKey(User,blank=True, null=True,on_delete=models.CASCADE)
    idFriends = models.CharField(max_length=200,null=True) 
    created = models.DateTimeField(auto_now=True)
    check = models.CharField(max_length=200,null=True) 

    def __str__(self):
        return self.idFriends
    
    class Meta:
        db_table = 'Friend'