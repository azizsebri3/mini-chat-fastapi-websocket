# Mini Chat Application - FastAPI WebSocket

A simple real-time chat application built using FastAPI and WebSockets. This application allows multiple users to connect to a WebSocket server, send and receive messages in real time, and select other users to chat with.

## Features

- Real-time messaging via WebSockets
- Select a user to chat with
- Multiple users can be connected at the same time
- Each user can only receive messages from the selected user
- Displays an active list of users to choose from for chatting

## Requirements

To run this application, you need Python 3.7 or higher. You also need to install the following dependencies:

- **FastAPI**: A modern web framework for building APIs with Python.
- **Uvicorn**: ASGI server for FastAPI to handle WebSocket connections.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/azizsebri3/mini-chat-fastapi-websocket.git
   cd mini-chat-fastapi-websocket
