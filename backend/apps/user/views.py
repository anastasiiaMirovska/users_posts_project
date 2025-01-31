# Create your views here.


from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from apps.auth.serializers import EmailSerializer
from apps.user.filters import UserFilter
from apps.user.serializers import ProfileSerializer, UserSerializer

UserModel = get_user_model()


class UserCreateView (CreateAPIView):
    """
    post:
    Creates user
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny,]


class UserListView (ListAPIView):
    """
    get:
        Returns a list of all users. Tis request returns data only if the user is authenticated
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = UserFilter


class UserRetrieveView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = self.request.data
        user_id = data.get('id')
        email = data.get('email')

        if not user_id and not email:
            return Response({"error": "Either 'id' or 'email' parameter is required"}, status=400)

        if user_id:
            user = get_object_or_404(UserModel, id=user_id)
        else:
            serializer = EmailSerializer(data={"email": email})
            serializer.is_valid(raise_exception=True)
            user = get_object_or_404(UserModel, email=serializer.validated_data['email'])

        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)


