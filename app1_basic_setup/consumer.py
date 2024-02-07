from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio


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
        print(f"{event['text']=}")

        for i in range(1, 21):
            self.send({
                "type": "websocket.send",
                "text": "Msg sync " + str(i),
            })
            sleep(0.3)

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
        for i in range(1, 21):
            await self.send({
                "type": "websocket.send",
                "text": "Msg sync " + str(i),
            })
            await asyncio.sleep(0.3)

    async def websocket_disconnect(self, event):
        '''this executed when connection closed.'''
        print("Websocker Disconnected...")
