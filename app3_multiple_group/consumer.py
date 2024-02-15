from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer


class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        '''this executed when client open a connection'''

        print("Websocker Connected...")
        print("self.channel_layer : ", self.channel_layer)
        print("self.channel_name : ", self.channel_name)

        await self.channel_layer.group_add(
            "python-group",
            self.channel_name
            )
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        '''this executed when data received from client'''

        print("Websocker Received...")
        print("Message received from client side.")
        print(event)
        print(event["text"])
        print(type(event["text"]))

        await self.channel_layer.group_send(
            "python-group",
            {
                'type': 'chat.message',
                'message': event['text']
            }
        )

    async def chat_message(self, event):
        print("Inside event")
        print("Event : ", event)
        print("Event : ", event['message'])
        print("Event : ", type(event['message']))

        await self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    async def websocket_disconnect(self, event):
        '''this executed when connection closed.'''

        print("Websocker Disconnected...")
        print("self.channel_layer : ", self.channel_layer)
        print("self.channel_name : ", self.channel_name)

        self.channel_layer.group_discard(
            "python-group",
            self.channel_name
            )

        raise StopConsumer
