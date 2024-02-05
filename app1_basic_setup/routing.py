from django.urls import path
from .consumer import MyAsyncConsumer, MySyncConsumer

websocket_urlpatterns = [
    path('ws/sync-call/', MySyncConsumer.as_asgi()),
    path('ws/async-call/', MyAsyncConsumer.as_asgi())
]
