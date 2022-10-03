import os
from channels.routing import ProtocolTypeRouter, URLRouter
import app.routing
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket_consumer.settings')

wsgi_app = get_asgi_application()
application = ProtocolTypeRouter({
	'http': wsgi_app,
	'websocket': AllowedHostsOriginValidator(
	AuthMiddlewareStack(
	URLRouter(
		app.routing.websocket_urlpatterns))
	)
	})
