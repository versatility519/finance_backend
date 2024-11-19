
from django.contrib.auth import authenticate
from rest_framework import serializers
# from django.contrib.auth.models import User

from .models import CustomUser as User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        

class SignupSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'role')

    def create(self, validated_data):
        # Create a new user and hash the password
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class SigninSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        # Lookup the user based on email
        user = User.objects.filter(email=email).first()
        
        print(user)
        
        # if not user.is_active:
        #     raise serializers.ValidationError("This account is inactive.")
        # if user is None or not user.check_password(password):
        #     raise serializers.ValidationError("Invalid credentials.")
        

        # Include the user in the validated data
        data['user'] = user
        return data