from django.http.response import HttpResponse
from rest_framework.decorators import api_view

from app import services


@api_view(['GET'])
def get_users(request):
    data = services.get_users(request.query_params)
    return HttpResponse(data.to_json(), content_type='application/json')


@api_view(['GET'])
def get_user_by_id(request, user_id):
    data = services.get_user_by_id(user_id)
    return HttpResponse(data.to_json(), content_type='application/json')


@api_view(['POST'])
def calculate(request):
    user = services.calculate(request.data)
    return HttpResponse(user.to_json(), content_type='application/json')


@api_view(['GET'])
def correlation(request):
    data = services.get_correlation(request.query_params)
    return HttpResponse(data.to_json(), content_type='application/json')
