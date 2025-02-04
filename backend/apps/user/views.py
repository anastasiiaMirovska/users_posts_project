from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.auth.serializers import EmailSerializer
from apps.user.filters import UserFilter
from apps.user.models import ProfileModel
from apps.user.serializers import ProfileSerializer, UserSerializer

UserModel = get_user_model()


class UserCreateView (CreateAPIView):
    """
    post:
    Creates user
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserListView (ListAPIView):
    """
    get:
        Returns a list of all users. This request returns data only if the user is authenticated
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = UserFilter


class UserDeleteView(GenericAPIView):
    """
    delete:
        Deletes user from database. User can delete only himself
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer(self):
        return None

    @atomic
    def delete(self, request, *args, **kwargs):
        user = request.user
        user_model = get_object_or_404(UserModel, pk=user.id)
        user_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class UserUpdateView(GenericAPIView):
    """
    patch:
        Updates user`s profile. User can update his profile
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    queryset = UserModel.objects.all()

    def patch(self, request, *args, **kwargs):
        profile = get_object_or_404(ProfileModel, user=self.request.user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveView(GenericAPIView):
    """
    get:
        Get user info by his id or email
    """
    queryset = UserModel.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer(self):
        return None

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

