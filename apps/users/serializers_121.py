from rest_framework import serializers
from .models import CustomUser as User

from rest_framework import serializers
# from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

# User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'role', 'email', 'fname', 'lname', 'is_active', 'date_joined']
#         read_only_fields = ['id', 'date_joined']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     return user
    
    def create(self, validated_data):
        groups_data = validated_data.pop('groups', [])
        user = User.objects.create_user(**validated_data)

        if  groups_data:
            user.groups.set(groups_data)
        return user

    def validate_password(self, value):
        # Add password validation logic here if needed
        return value

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['fname', 'lname', 'email']

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is not correct")
        return value

    def validate_new_password(self, value):
        # Add password validation logic here if needed
        return value

    def save(self, **kwargs):
        password = self.validated_data['new_password']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user
 