from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    password = serializers.RegexField(
        regex=("^(?=.{8,}$)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*"),
        min_length=8,
        max_length=30,
        required=True,
        write_only=True,
        error_messages={
            'required': 'Password is a required field',
            'min_length': 'Password must be at least 8 characters long',
            'max_length': 'Password cannot be more than 30 characters',
            'invalid': 'Password must have at least a number, and a least an uppercase and a lowercase letter',
        }
    )

    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='Email is already in use by another user'
            )
        ],
        error_messages={
            'invalid': 'Email must be of the format name@domain.com',
            'required': 'Email is a required field'
        }
    )

    id = serializers.IntegerField( read_only=True )

    created_at = serializers.DateTimeField( read_only=True )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'id', 'created_at', 'token')

    @classmethod
    def create(cls, data):
        return User.objects.create_user(**data)

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):

        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        return {
            'email': user.email,
            'token': user.token

        }
        return instance
