from django.db import models

# Create your models here.
# chat/models.py
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} to {self.receiver}: {self.message}'

class info(models.Model):
    id = models.AutoField(primary_key=True)
    whoiswho =  models.CharField(max_length=1000,default = 'whoiswho')
    to = models.CharField(max_length=1000,default = '')#name of stage  
    writer =models.CharField(max_length=1000, blank=True, default='anonymous')#
    mation = models.CharField(max_length=10000000,default = '')  
    title =  models.CharField(max_length=1000,default = 'notitle')
    image = models.ImageField(upload_to= 'files/',null = True)
    delete = models.CharField(max_length=1000,default = 'no')
    date = models.CharField(max_length=1000,default = 'no date')    #
    class Meta:
        ordering =['id']    