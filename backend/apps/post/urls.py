from django.urls import path

from apps.post.views import (
    PostListCreateView,
    PostPhotoRetrieveUpdateDestroyView,
    PostPhotosListCreateView,
    PostRetrieveUpdateDestroyView
)

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post_list_create'),
    path('/<int:pk>', PostRetrieveUpdateDestroyView.as_view(), name='post_retrieve_update_delete'),
    path('/<int:pk>/photos', PostPhotosListCreateView.as_view(), name='post_photos_list_create'),
    path('/<int:pk>/photos/<int:photo_id>', PostPhotoRetrieveUpdateDestroyView.as_view(), name='post_photos_retrieve_update_delete')
    # path('/update', PostUpdateView.as_view(), name='post_update'),
    # path('/delete', PostDeleteView.as_view(), name='post_delete')
]

