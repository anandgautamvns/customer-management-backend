from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from .serializers import UserRegisterSerializer, UserProfileSerializer, CustomTokenObtainPairSerializer

User = get_user_model()

class UserRegisterView(generics.CreateAPIView):
    """API for user registration."""
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(TokenObtainPairView):
    """Custom Login View using JWT."""
    serializer_class = CustomTokenObtainPairSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    """User Profile API (Authenticated Users)"""
    queryset = User.objects.all().select_related()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class LogoutView(generics.GenericAPIView):
    """Logout API - Blacklists refresh token"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh_token")
        if not refresh_token:
            return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)