from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=6,
        style={'input_type': 'password'},
        validators=[validate_password]
    )
    confirm_password = serializers.CharField(
        write_only=True,
        min_length=6,
        # style={'input_type': 'password'},
        validators=[validate_password]
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password', 'confirm_password']

    def validate_email(self, value):
        """Ensure email is unique."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered.")
        return value

    def validate_username(self, value):
        """Ensure username is unique."""
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

    def validate(self, data):
        """Ensure passwords match."""
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data
      
    def create(self, validated_data):
        """Create user with hashed password."""
        validated_data.pop("confirm_password")  # Remove confirm_password from data
        user = User.objects.create_user(**validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for viewing & updating user profile."""
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom JWT Token Serializer - Includes email in token."""
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['email'] = user.email
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Get token for the user
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add user details to the response
        data['user'] = {
            'id': self.user.id,
            'email': self.user.email,
            'username': self.user.username,
            # Add additional fields as needed
        },
        data['token'] = str(refresh.access_token)
        return data