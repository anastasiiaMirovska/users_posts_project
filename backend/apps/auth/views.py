from datetime import datetime

from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken, SocketToken

from apps.auth.serializers import EmailSerializer, PasswordSerializer
from apps.user.serializers import UserSerializer

UserModel = get_user_model()


class CustomTokenRefreshView(TokenRefreshView):
    """
    post:
    Blacklists old refresh token and puts new refresh token into token_blacklist_outstanding_token
    """
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        data = response.data

        old_refresh_token = request.data.get("refresh")
        if old_refresh_token:
            try:
                token = RefreshToken(old_refresh_token)
                token.blacklist()
            except Exception as e:
                print(f"Не вдалося занести токен у blacklist: {e}")

        new_refresh_token = data.get("refresh")
        if new_refresh_token:
            try:
                new_token = RefreshToken(new_refresh_token)
                jti = new_token.payload["jti"]
                expires_at = datetime.fromtimestamp(int(new_token.access_token.payload["exp"]))

                OutstandingToken.objects.get_or_create(
                    jti=jti,
                    defaults={
                        "token": new_refresh_token,
                        "created_at": datetime.now(),
                        "user_id": self.request.user.id,
                        "expires_at": expires_at
                    }
                )
            except Exception as e:
                print(f"Error while saving new token: {e}")

        return response


class ActivateUserView(GenericAPIView):
    """
    patch:
    Makes user authorized by setting is_active=True
    """
    permission_classes = [AllowAny]

    def patch(self, request, *args, **kwargs):
        token = kwargs['token']
        user = JWTService.verify_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RecoveryRequestView(GenericAPIView):
    """
    Sends letter with recovery token
    """
    permission_classes = [AllowAny]

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = EmailSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, email=serializer.data['email'])
        EmailService.recovery(user)
        return Response({'detail': 'Link was sent to your email'}, status=status.HTTP_200_OK)


class RecoveryPasswordView(GenericAPIView):
    """
    patch:
    Sets new user password entered by user
    """
    permission_classes = [AllowAny]

    def patch(self, *args, **kwargs):
        data = self.request.data
        serializer = PasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        token = kwargs['token']
        user = JWTService.verify_token(token, RecoveryToken)
        user.set_password(serializer.data['password'])
        user.save()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)


class UserLogoutView(GenericAPIView):
    """
    post:
    Blacklists the refresh token, lets new last_logout value
    """
    permission_classes = [IsAuthenticated]
    def post(self,request, *args, **kwargs):
        try:
            refresh_token = self.request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            user = request.user
            user.last_logout = datetime.now()
            user.save()
            return Response({"detail": "Session ended"}, status=status.HTTP_205_RESET_CONTENT)

        except Exception as e:
            return Response({"error": "No refresh token provided"}, status=status.HTTP_400_BAD_REQUEST)


class SocketTokenView(GenericAPIView):
    """
    get:
    Creates a new token
    """
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        token = JWTService.create_token(self.request.user, SocketToken)
        return Response({'token': str(token)}, status=status.HTTP_200_OK)



