from rest_framework.permissions import BasePermission, IsAuthenticated

from apps.post.models import PostModel, PostPhotoModel


class IsPostOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.user.is_superuser or obj.author == request.user


class IsPostPhotoOwnerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST" or request.method == "PUT" or request.method == "PATCH" or request.method == "DELETE":
            post_id = view.kwargs.get("pk")
            post = PostModel.objects.filter(id=post_id).first()
            return post and (request.user == post.author or request.user.is_staff or request.user.is_superuser)
        return request.method in ["GET", "HEAD", "OPTIONS"]

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.user.is_superuser or obj.post.author == request.user


class IsProfileOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.user.is_superuser or request.user == obj

