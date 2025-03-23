import json
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()

# Dictionnaire pour garder la connexion WebSocket de chaque utilisateur
active_connections: dict = {}

# Liste d'utilisateurs simulée (vous pouvez la remplacer par une base de données ou une autre source dynamique)
users = ["user1", "user2", "user3"]

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    # Accepter la connexion WebSocket
    await websocket.accept()
    active_connections[username] = websocket  # Enregistrer la connexion WebSocket du client

    try:
        # Envoyer la liste des utilisateurs au client dès la connexion
        await websocket.send_json({"type": "user_list", "users":list(active_connections.keys())})

        while True:
            # Attendre et recevoir des messages
            data = await websocket.receive_text()
            message_data = json.loads(data)
            receiver = message_data.get("receiver")
            message = message_data.get("message")

            # Envoyer le message au destinataire s'il est connecté
            if receiver in active_connections:
                await active_connections[receiver].send_text(json.dumps({
                    "sender": username,
                    "message": message
                }))
            else:
                print(f"Utilisateur {receiver} n'est pas connecté.")
                
    except WebSocketDisconnect:
        # Supprimer la connexion WebSocket lorsque l'utilisateur se déconnecte
        active_connections.pop(username, None)
        print(f"{username} a quitté la conversation.")
