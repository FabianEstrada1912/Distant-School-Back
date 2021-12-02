from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Cons(models.Model):
    sender = models.ForeignKey(User,blank=True, null=True,on_delete=models.CASCADE)
    receiver = models.CharField(max_length=200,null=True) 
    mensaje = models.CharField(max_length=250,null=True) 
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.mensaje

    class Meta:
        db_table = 'Cons'