from django.shortcuts import render
from cgitb import lookup
from django.shortcuts import render
#from matplotlib.pyplot import table
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
# Create your views here.
class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer          
 
class clientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = clientSerializer

    def perform_create(self, serializer):
        serializer.save()
class clientDetail(generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'pk'
    queryset = Client.objects.all()
    serializer_class = clientSerializer
class lawyerList(generics.ListCreateAPIView):
    queryset = lawyer.objects.all()
    serializer_class = lawyerSerializer

    def perform_create(self, serializer):
        serializer.save()
class lawyerDetail(generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'pk'
    queryset = lawyer.objects.all()
    serializer_class = lawyerSerializer
class lawfirmList(generics.ListCreateAPIView):
    queryset = lawfirm.objects.all()
    serializer_class = lawfirmSerializer

    def perform_create(self, serializer):
        serializer.save()
class lawfirmDetail(generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'pk'
    queryset = lawfirm.objects.all()
    serializer_class = lawfirmSerializer
class verifiedList(generics.ListCreateAPIView):
    queryset = verified.objects.all()
    serializer_class = verifiedSerializer

    def perform_create(self, serializer):
        serializer.save()
class verifiedDetail(generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'pk'
    queryset = verified.objects.all()
    serializer_class = verifiedSerializer
class rartingList(generics.ListCreateAPIView):
    queryset = rating.objects.all()
    serializer_class = ratingSerializer

    def perform_create(self, serializer):
        serializer.save()
class rartingDetail(generics.ListCreateAPIView):
    queryset = rating.objects.all()
    serializer_class = ratingSerializer

    
class activeList(generics.ListCreateAPIView):
    queryset = active.objects.all()
    serializer_class = activateSerializer

    def perform_create(self, serializer):
        serializer.save()
class activeDetail(generics.ListCreateAPIView):
    queryset = active.objects.all()
    serializer_class = activateSerializer
class profileList(generics.ListCreateAPIView):
    queryset = ProfilePicture.objects.all()
    serializer_class = profilepictureSerializer

    def perform_create(self, serializer):
        serializer.save()
class profileDetail(generics.ListCreateAPIView):
    queryset = ProfilePicture.objects.all()
    serializer_class = profilepictureSerializer
