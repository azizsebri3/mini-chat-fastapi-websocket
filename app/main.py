import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List, Dict

app = FastAPI()


active_connections: Dict = {}

messages_history: Dict[str, List[Dict[str, str]]] = {}

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await websocket.accept()
    print(f"{username} is connected now!")
    active_connections[username] = websocket

    await websocket.send_json({
        "type": "user_list",
        "users": [user for user in active_connections.keys() if user != username]
    })

    
    if username in messages_history:
        for msg in messages_history[username]:
            await websocket.send_json(msg)

    try:
        while True:
            #wait the message from the client 
            data = await websocket.receive_text()
            message_data = json.loads(data)
            receiver = message_data.get("receiver")
            message = message_data.get("message")

            #save the message in the history to retrieve it later
            if receiver not in messages_history:
                messages_history[receiver] = []
            messages_history[receiver].append({
                "sender": username,
                "message": message
            })

            #send the message to the receiver if he is connected
            if receiver in active_connections:
                await active_connections[receiver].send_text(json.dumps({
                    "sender": username,
                    "message": message
                }))
            else:
                print(f"L'utilisateur {receiver} n'est pas connecté.")
                
    except WebSocketDisconnect:
        # delete the user from the active connections if he disconnect
        active_connections.pop(username, None)
        print(f"{username} a quitté la conversation.")
