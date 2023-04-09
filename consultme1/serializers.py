from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class clientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id','username']

class lawyerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = lawyer
        fields = ['id','owner','firstnamex','Secondnamex','meimagex','company','Sdescription','Ldescription','quoterange','licensenumber']
class categorySerializer(serializers.ModelSerializer):
    lawyers = lawyerSerializer(many=True)
    class Meta:
        model = Categry
        fields = ['name','lawyers','Ldescription']
class lawfirmSerializer(serializers.ModelSerializer):
    lawyers = lawyerSerializer(many=True)
    class Meta:
        model = lawfirm
        fields = ['name','lawyers','Ldescription']
class verifiedSerializer(serializers.ModelSerializer):
    class Meta:
        model = verified
        fields = ['username','typeofverification']
class ratingSerializer(serializers.ModelSerializer):
    class Meta:
        model = verified
        fields = ['username','typeofverification']
class activateSerializer(serializers.ModelSerializer):
    class Meta:
        model = verified
        fields = ['username','typeof','timeaactive']
class profilepictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = verified
        fields = ['username','typeof']

class RegisterSerializer(serializers.ModelSerializer,):
    permission_classes = []
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user        