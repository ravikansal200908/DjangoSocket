from channels.consumer import SyncConsumer, AsyncConsumer


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
            "text": event["text"],
        })

    def websocket_disconnect(self, event):
        '''this executed when connection closed.'''
        print("Websocker Disconnected...", event)


class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        '''this executed when client open a connection'''
        print("Websocker Connected...")

    async def websocket_receive(self, event):
        '''this executed when data received from client'''
        print("Websocker Received...")

    async def websocket_disconnect(self, event):
        '''this executed when connection closed.'''
        print("Websocker Disconnected...")
