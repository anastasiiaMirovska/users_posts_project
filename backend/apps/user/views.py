# Create your views here.


from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.user.serializers import UserSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

