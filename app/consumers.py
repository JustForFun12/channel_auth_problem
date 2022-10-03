from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import time
import asyncio
from pprint import pprint
from asgiref.sync import async_to_sync

class MyWebsocketConsumer(WebsocketConsumer):
	def connect(self):
		print("connected")
		pprint(self.scope)
		pprint(self.scope['user'].username)
		
		self.room_name = self.scope['url_route']['kwargs']['room']
		group_add = async_to_sync(self.channel_layer.group_add)
		group_add(self.room_name, self.channel_name)

		self.accept()

	def receive(self, text_data=None, bytes_data=None):
		pprint(self.scope['user'].is_authenticated)
		print('msg received', text_data)

		group_send = async_to_sync(self.channel_layer.group_send)
		message = {
		'type': 'chat.message',
		'msg': text_data
		}
		group_send(self.room_name, message)

		# self.send(text_data)

	def chat_message(self, event):
		msg = event['msg']
		self.send(msg)

	def disconnect(self, close_code):
		print("disconnected", close_code)






















'''
class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		print("connected")
		await self.accept()

	async def receive(self, text_data=None, bytes_data=None):
		print('msg received')
		for i in range(20):
			await self.send(text_data=str(i))
			await asyncio.sleep(1)

	async def disconnect(self, close_code):
		print("disconnected", close_code)
'''