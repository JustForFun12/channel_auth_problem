from django.urls import path
from . import consumers

websocket_urlpatterns = [
	path('ws/wsc/<str:room>', consumers.MyWebsocketConsumer.as_asgi()),
	# path('ws/awsc/', consumers.MyAsyncWebsocketConsumer.as_asgi())


]