from django.urls import path

from apps.user.views import UserCreateView, UserDeleteView, UserListView, UserRetrieveView, UserUpdateView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('/create', UserCreateView.as_view(), name='user_create'),
    path('/find', UserRetrieveView.as_view(), name='user_retrieve_by_id_or_email'),
    path('/update', UserUpdateView.as_view(), name='user_update'),
    path('/delete', UserDeleteView.as_view(), name='user_delete'),
]
