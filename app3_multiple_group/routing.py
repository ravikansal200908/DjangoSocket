from django.urls import path
from .consumer import MyAsyncConsumer

socket_urls = [
    path('ws/async-call/channel/', MyAsyncConsumer.as_asgi())
]
