from .models import *


def get_users(query_params):
    return User.objects.filter(**query_params.dict())


def get_user_by_id(user_id):
    return User.objects.get(user_id=user_id)


def get_correlation(query_params):
    return CorrelationResults.objects.filter(**query_params.dict())


def calculate(user_data):
    user = User(**user_data)
    user = user.save()
    calculate_correlation(user['_id'])
    return user


def calculate_correlation(_id):
    pass
