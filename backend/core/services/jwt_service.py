from typing import Type

from rest_framework_simplejwt.tokens import BlacklistMixin, Token

from django.contrib.auth import get_user_model

from rest_framework.generics import get_object_or_404

from core.enums.action_token_enum import ActionTokenEnum
from core.exceptions.jwt_exception import JWTException

UserModel = get_user_model()
ActionTokenClassType = Type[BlacklistMixin | Token]


class ActionToken(BlacklistMixin, Token):
    pass


class ActivateToken(ActionToken):
    token_type = ActionTokenEnum.ACTIVATE.token_type
    lifetime = ActionTokenEnum.ACTIVATE.lifetime


class RecoveryToken(ActionToken):
    token_type = ActionTokenEnum.RECOVERY.token_type
    lifetime = ActionTokenEnum.RECOVERY.lifetime


class SocketToken(ActionToken):
    token_type = ActionTokenEnum.SOCKET.token_type
    lifetime = ActionTokenEnum.SOCKET.lifetime

class JWTService:
    @staticmethod
    def create_token(user, token_class: ActionTokenClassType):
        return token_class.for_user(user)

    @staticmethod
    def verify_token(token, token_class: ActionTokenClassType):
        try:
            token_res = token_class(token)  # Декодує токен
            token_res.check_blacklist()  # Перевіряє, чи токен не в чорному списку
        except Exception:
            raise JWTException

        token_res.blacklist()  # Додає токен до чорного списку
        user_id = token_res.payload.get('user_id')  # Отримує ID користувача з токена
        return get_object_or_404(UserModel, pk=user_id)  # Повертає об'єкт користувача

