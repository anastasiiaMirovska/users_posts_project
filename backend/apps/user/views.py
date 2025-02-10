from drf_yasg.utils import swagger_auto_schema

from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.generics import DestroyAPIView, GenericAPIView, ListCreateAPIView, UpdateAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.auth.serializers import EmailSerializer
from apps.user.filters import UserFilter
from apps.user.models import ProfileModel
from apps.user.permissions import IsProfileOwnerOrAdmin
from apps.user.serializers import ProfileSerializer, UserPhotoSerializer, UserSerializer

UserModel = get_user_model()

@method_decorator(
    name='post',
    decorator=swagger_auto_schema(
        security=[]
    )
)
class UserListCreateView(ListCreateAPIView):
    """
    get:
        Returns a list of all users. This request returns data only if the user is authenticated
    post:
        Creates user
    """
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        if self.request.method == 'POST':
            return [AllowAny()]
        return [IsAdminUser()]


class UserUpdateDestroyView(UpdateAPIView, DestroyAPIView):
    """
    put:
        Updates user profile(full). It can be done only by profile owner,admin or superuser
    patch:
        Partially updates user profile. It can be done only by profile owner,admin or superuser
    delete:
        Deletes user from DB. It can be done only by profile owner, admin or superuser
    """

    serializer_class = UserSerializer
    permission_classes = [IsProfileOwnerOrAdmin, IsAuthenticated]
    queryset = UserModel.objects.all()
    http_method_names = ['put', 'patch', 'delete']

    # def get_object(self):
    #     obj = super().get_object()
    #     if self.request.user.is_staff or self.request.user.is_superuser or self.request.user == obj:
    #         return obj
    #     else:
    #         self.permission_denied(
    #             self.request,
    #             message="You do not have permission to access this user."
    #         )

    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        profile = get_object_or_404(ProfileModel, user=user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        profile = get_object_or_404(ProfileModel, user=user)
        serializer = ProfileSerializer(profile, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        self.perform_destroy(user)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfileAddPhotoView(GenericAPIView):
    """
    put:
        Sets user photo profile. Such photo can be only one, so every time you send this request, the previous photo deletes and new one sets
    """
    serializer_class = UserPhotoSerializer
    permission_classes = [IsProfileOwnerOrAdmin, IsAuthenticated]
    queryset = UserModel.objects.all()
    http_method_names = ['put']

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        profile = get_object_or_404(ProfileModel, user=user)
        profile.photo.delete()
        photo_serializer = UserPhotoSerializer(profile, data=request.data)
        photo_serializer.is_valid(raise_exception=True)
        photo_serializer.save()
        return Response(photo_serializer.data, status=status.HTTP_200_OK)



class UserRetrieveView(GenericAPIView):
    """
    get:
        Get user info by his id or email. It can also be done by the request to api/users
    """
    queryset = UserModel.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']

    def get_serializer(self):
        return None

    def get(self, request, *args, **kwargs):
        user_id = request.GET.get('id')
        email = request.GET.get('email')

        if not user_id and not email:
            return Response({"error": "Either 'id' or 'email' parameter is required"}, status=400)

        if user_id:
            user = get_object_or_404(UserModel, id=user_id)
        else:
            serializer = EmailSerializer(data={"email": email})
            serializer.is_valid(raise_exception=True)
            user = get_object_or_404(UserModel, email=serializer.validated_data['email'])

        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)



# class UserDeleteView(GenericAPIView):
#     """
#     delete:
#         Deletes user from database. User can delete only himself
#     """
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_serializer(self):
#         return None
#
#     @atomic
#     def delete(self, request, *args, **kwargs):
#         user = request.user
#         user_model = get_object_or_404(UserModel, pk=user.id)
#         user_model.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# class UserUpdateView(GenericAPIView):
#     """
#     patch:
#         Updates user`s profile. User can update his profile
#     """
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]
#     queryset = UserModel.objects.all()
#
#     def patch(self, request, *args, **kwargs):
#         profile = get_object_or_404(ProfileModel, user=self.request.user)
#         serializer = ProfileSerializer(profile, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)



# class UserCreateView (CreateAPIView):
#     """
#     post:
#     Creates user
#     """
#     queryset = UserModel.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]
#
#
# class UserListView (ListAPIView):
#     """
#     get:
#         Returns a list of all users. This request returns data only if the user is authenticated
#     """
#     queryset = UserModel.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]
#     filterset_class = UserFilter


