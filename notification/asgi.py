import os
from django.core.asgi import get_asgi_application
from channels.routing import URLRouter , ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notification.settings')
from core.routing import ws_urlpatterns

# application = get_asgi_application()

# application= ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket' : AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(
#         ws_urlpatterns,
#     )))
# })


application= ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket' : AuthMiddlewareStack(URLRouter(ws_urlpatterns,))
})
