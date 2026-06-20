class ConnectionManager:

    def __init__(self):
        self.active={}

    async def connect(self,user_id,ws):
        await ws.accept()
        self.active[user_id]=ws

    def disconnect(self,user_id):
        if user_id in self.active:
            del self.active[user_id]

    async def send_private(self,user_id,data):
        if user_id in self.active:
            await self.active[user_id].send_json(data)

manager=ConnectionManager()
