# chat/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import *
from .serializers import *
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatView(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'chat'
        self.room_group_name = f'chat_{self.room_name}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        serializer = ChatMessageSerializer(data=data)
        if serializer.is_valid():
            chat_message = await database_sync_to_async(serializer.save)()
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': ChatMessageSerializer(chat_message).data
                }
            )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(message))
class ChatMessageListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChatMessageSerializer

    def get_queryset(self):
        queryset = ChatMessage.objects.filter(sender=self.request.user) | ChatMessage.objects.filter(receiver=self.request.user)
        return queryset.order_by('-timestamp')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        chat_message = serializer.save(sender=self.request.user)
        receiver = chat_message.receiver
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'chat_{receiver.id}',
            {
                'type': 'chat_message',
                'id': chat_message.id,
                'sender': chat_message.sender.username,
                'receiver': chat_message.receiver.username,
                'message': chat_message.message,
                'timestamp': chat_message.timestamp.isoformat()
            }
        )
        return Response(serializer.data)
class userffDetail(generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'pk'
    queryset = User.objects.all()
    serializer_class = userfSerializer
class infoList(generics.ListCreateAPIView):
    #permission_classes = (AllowAny,)
    queryset = info.objects.all()
    serializer_class = infoSerializer
    def perform_create(self, serializer):
        serializer.save()      
        return render(self, 'pic.html',{'movie': queryset})
