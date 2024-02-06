from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer


class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        '''this executed when client open a connection'''
        print("Websocker Connected...", event)
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        '''this executed when data received from client'''
        print("Websocker Received...", event)
        self.send({
            "type": "websocket.send",
            "text": event["text"] + " sync",
        })

    def websocket_disconnect(self, event):
        '''this executed when connection closed.'''
        print("Websocker Disconnected...", event)
        raise StopConsumer


class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        '''this executed when client open a connection'''
        print("Websocker Connected...")
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        '''this executed when data received from client'''
        print("Websocker Received...")
        await self.send({
            "type": "websocket.send",
            "text": event["text"] + " async",
        })

    async def websocket_disconnect(self, event):
        '''this executed when connection closed.'''
        print("Websocker Disconnected...")
