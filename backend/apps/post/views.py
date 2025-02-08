from drf_yasg.utils import swagger_auto_schema

from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.generics import DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.post.models import PostModel, PostPhotoModel
from apps.post.serializers import PostPhotoSerializer, PostSerializer
from apps.user.permissions import IsPostOwnerOrAdmin, IsPostPhotoOwnerOrAdmin


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        security=[]
    )
)
class PostListCreateView(ListCreateAPIView):
    """
    get:
        Returns a list of posts. It can be done by anyone, even by unauthenticated users. You can also filter it by author
    post:
        Creates a new post for user
    """
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()
    permission_classes = [IsAuthenticated]
    filterset_fields = ['author']
    http_method_names = ['get', 'post']

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        security=[]
    )
)
class PostRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns a post.It can be done by anyone, even by unauthenticated users.
    put:
        Updates a post (full). It can be done only by post owner, admin or superuser
    patch:
        Partially updates a post. It can be done only by post owner, admin or superuser
    delete:
    Deletes a post. It can be done only by post owner, admin or superuser
    """
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsPostOwnerOrAdmin, IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = PostSerializer(post, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        self.perform_destroy(post)
        return Response(status=status.HTTP_204_NO_CONTENT)


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        security=[]
    )
)
class PostPhotosListCreateView(ListCreateAPIView):
    """
    get:
        Returns a list of all post photos. It can be done by anyone, even by unauthenticated users.
    post:
        Creates a new post photo. You can add many photos to a post. It can be done only by post photo owner, admin or superuser
    """
    serializer_class = PostPhotoSerializer
    permission_classes = [IsPostPhotoOwnerOrAdmin]

    def get_queryset(self):
        return PostPhotoModel.objects.filter(post_id=self.kwargs['pk'])

    def perform_create(self, serializer):
        post_id = self.kwargs.get('pk')
        post = PostModel.objects.filter(id=post_id).first()
        if not post or (self.request.user != post.author and not self.request.user.is_staff and not self.request.user.is_superuser):
            raise PermissionDenied("You do not have permission to add photos to this post.")
        serializer.save(post_id=post_id)


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(
        security=[]
    )
)
class PostPhotoRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Returns a single post photo. It can be done by anyone, even by unauthenticated users.
    put:
        Updates a post photo. It can be done only by post photo owner, admin or superuser
    delete:
        Deletes a post photo. It can be done by post photo owner, admin or superuser
    """

    serializer_class = PostPhotoSerializer
    permission_classes = [IsPostPhotoOwnerOrAdmin, IsAuthenticated]
    http_method_names = ['get', 'put', 'delete']

    def get_object(self):
        post_id = self.kwargs.get('pk')
        photo_id = self.kwargs.get('photo_id')

        try:
            return PostPhotoModel.objects.get(post_id=post_id, id=photo_id)
        except PostPhotoModel.DoesNotExist:
            raise NotFound(detail="Photo not found for this post")


# class PostPhotosListCreateView(ListCreateAPIView):
#     serializer_class = PostPhotoSerializer
#     permission_classes = [IsPostOwnerOrAdmin]
#
#     def get_queryset(self, *args, **kwargs):
#         queryset = PostPhotoModel.objects.all().filter(post_id=self.kwargs['pk'])
#         return queryset
#
#     def get(self, request, *args, **kwargs):
#         photos = self.get_queryset()
#         serializer = self.get_serializer(photos, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(post_id=kwargs.get('pk'))
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

