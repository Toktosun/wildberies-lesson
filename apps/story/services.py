from django.contrib.auth.models import User

from apps.story.api_exceptions import UnauthorizedResponseException, \
    ForbiddenResponseException


class ProfileAuthService:
    """Обслуживащий класс для работы с авторизациями пользователей"""

    @classmethod
    def get_user_by_headers(cls, headers: dict):
        try:
            token = headers['HTTP_AUTHORIZATION']
        except KeyError:
            raise UnauthorizedResponseException

        try:
            user = User.objects.get(token=token)
        except User.DoesNotExist:
            raise ForbiddenResponseException
        return user


class TelegramMessageService:

    @classmethod
    def send_message_to_user(cls, username: str):
        print('Здесь будет блок по отправке сообщения в телеграм')
        print('Здесь будет блок по отправке сообщения в телеграм')
        print('Здесь будет блок по отправке сообщения в телеграм')
        print('Здесь будет блок по отправке сообщения в телеграм')
        print('Здесь будет блок по отправке сообщения в телеграм')
        print('Здесь будет блок по отправке сообщения в телеграм')
        print('Здесь будет блок по отправке сообщения в телеграм')
        print('Здесь будет блок по отправке сообщения в телеграм')
        print('Здесь будет блок по отправке сообщения в телеграм')
        print('Здесь будет блок по отправке сообщения в телеграм')