from fastapi import FastAPI,WebSocket,WebSocketDisconnect
from routes import router
from websocket_manager import manager
import json

app=FastAPI()

app.include_router(router)

@app.websocket("/ws/{user_id}")
async def websocket(ws:WebSocket,user_id:int):

    await manager.connect(user_id,ws)

    try:
        while True:

            data=await ws.receive_text()
            data=json.loads(data)

            to=data["to"]

            await manager.send_private(to,{
                "from":user_id,
                "message":data["message"],
                "type":data["type"]
            })

    except WebSocketDisconnect:
        manager.disconnect(user_id)
