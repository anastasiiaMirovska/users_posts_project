
from django.urls import path

from apps.user.views import ProfileAddPhotoView, UserListCreateView, UserUpdateDestroyView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_retrieve_list_create'),
    path('/<int:pk>', UserUpdateDestroyView.as_view(), name='user_update_destroy'),
    path('/<int:pk>/photo', ProfileAddPhotoView.as_view(), name='user_profile_photo')
    

    # path('/find', UserRetrieveView.as_view(), name='user_retrieve_by_id_or_email'),
    # path('/create', UserCreateView.as_view(), name='user_create'),
    # path('/update', UserUpdateView.as_view(), name='user_update'),
    # path('/delete', UserDeleteView.as_view(), name='user_delete'),
]

