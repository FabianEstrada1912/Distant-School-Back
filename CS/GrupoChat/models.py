from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    user =  models.ForeignKey(User,blank=True, null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True) 
    created = models.DateTimeField(auto_now=True)
    descripcion = models.CharField(max_length=200,null=True)
     

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Chat'