import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from app1_basic_setup.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoSocket.settings")

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        websocket_urlpatterns
    )
})
