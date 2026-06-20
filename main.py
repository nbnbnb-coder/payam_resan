from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

connections = {}

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await websocket.accept()
    connections[username] = websocket

    try:
        while True:
            data = await websocket.receive_json()
            to_user = data["to"]
            message = data["message"]

            if to_user in connections:
                await connections[to_user].send_json({
                    "from": username,
                    "message": message
                })

    except WebSocketDisconnect:
        connections.pop(username, None)
