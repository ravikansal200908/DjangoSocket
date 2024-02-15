from django.urls import path
from .consumer import MyAsyncConsumer

socket_urls = [
    path('ws/group/<str:group_name>/', MyAsyncConsumer.as_asgi())
]
