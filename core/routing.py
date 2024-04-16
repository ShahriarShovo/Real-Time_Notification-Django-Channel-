from django.urls import path
from core.consumers import NotificationConsumers


ws_urlpatterns = [
    path('notifications/', NotificationConsumers.as_asgi()),
]