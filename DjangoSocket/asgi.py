import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from app1_basic_setup.routing import websocket_urlpatterns
from app2_channel_group.routing import socket_urls

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSocket.settings")

websocket_urlpatterns = socket_urls + websocket_urlpatterns

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        websocket_urlpatterns
    )
})
