from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path

from apps.auth.views import ActivateUserView, RecoveryPasswordView, RecoveryRequestView, SocketTokenView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/activate/<str:token>', ActivateUserView.as_view(), name='activate_user'),
    path('/recovery', RecoveryRequestView.as_view(), name='auth_recovery'),
    path('/recovery/<str:token>', RecoveryPasswordView.as_view(), name='auth_recovery_password'),
    path('/socket', SocketTokenView.as_view(), name='get_socket_token')
]

