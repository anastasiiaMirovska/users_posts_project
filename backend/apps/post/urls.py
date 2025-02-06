from django.urls import path

from apps.post.views import (
    PostListCreateView,
    PostPhotoRetrieveUpdateDestroyView,
    PostPhotosListCreateView,
    PostUpdateDestroyView
)

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post_retrieve_list_create'),
    path('/<int:pk>', PostUpdateDestroyView.as_view(), name='post_update_delete'),
    path('/<int:pk>/photos', PostPhotosListCreateView.as_view(), name='post_photos_list_create'),
    path('/<int:pk>/photos/<int:photo_id>', PostPhotoRetrieveUpdateDestroyView.as_view(), name='post_photos_retrieve_update_delete')
    # path('/update', PostUpdateView.as_view(), name='post_update'),
    # path('/delete', PostDeleteView.as_view(), name='post_delete')
]

