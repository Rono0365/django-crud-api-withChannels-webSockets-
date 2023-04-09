from rest_framework import serializers

from rest_framework import serializers
from .models import *

class ChatMessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField(read_only=True)
    recipient = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ChatMessage
        fields = ['id', 'sender', 'recipient', 'content', 'timestamp']
class userfSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','id']
class infoSerializer(serializers.ModelSerializer):
    #permission_classes = (AllowAny,)
    #image=serializers.ImageField(max_length=200,use_url=True)
    class Meta:
        model = info
        fields = ['id','to','whoiswho','writer','mation','image','title','date']