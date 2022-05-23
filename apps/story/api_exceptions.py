from rest_framework import status
from rest_framework.exceptions import APIException


class UnauthorizedResponseException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'Вы не передаёте токен в заголовке Authorization'


class ForbiddenResponseException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'У вас невалидный токен'