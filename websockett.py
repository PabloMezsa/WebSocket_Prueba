# import requests
# tm=0
# pr=0
# def get_data_from_server(tm,pr):  # Aceptar un argumento opcional
#     url = 'http://localhost:5000/get_data'
#     response = requests.get(url)
#     data = response.json()
#     return [data['temperature'], data['pressure']]

# temperature, pressure = get_data_from_server(tm, pr)
# print(temperature, pressure)

# import asyncio
# import websockets

# async def main():
#     uri = "ws://localhost:5000/socket.io/?EIO=4&transport=websocket"
#     async with websockets.connect(uri) as websocket:
#         message_to_send = "Hello, server!"
#         await websocket.send(message_to_send)
#         print(f"Sent message to server: {message_to_send}")

#         response = await websocket.recv()
#         print(f"Received message from server: {response}")

# asyncio.run(main())
# import socketio
# import asyncio
# import random
# import string
# text = ""
# # def generate_random_text(length=10):
# #     letters = string.ascii_letters
# #     return ''.join(random.choice(letters) for _ in range(length))

# def main(text):

#     sio = socketio.Client(text)
#     received_message = ""

#     @sio.event
#     def connect():
#         print('Connection established')

#     @sio.event
#     def message_from_server(data):
#         nonlocal received_message
#         received_message = data
#         print('Message from server:', data)
#         sio.disconnect()

#     @sio.event
#     def disconnect():
#         print('Disconnected from server')

#     random_text = text
#     sio.connect('http://localhost:5000')
#     #'Hello, server!'
#     sio.emit('message_from_client', text)
#     #sio.wait()
#     #print("message = ",received_message)
    
#     return random_text

# # Ejecutar la función principal y obtener el resultado
# if __name__ == "__main__":
#     result = main()
#     print("Result:", result)

import socketio
import asyncio
import random
import string

sio = socketio.Client()

def instant():
    
    sio.connect('http://localhost:5000')
    return "Establecida"

def main():
  
    @sio.event
    def connect():
         print('connection established')

    return 'connection established'

def main_2():
    
    received_message = ""

    @sio.event
    def message_from_server(data):
        nonlocal received_message
        received_message = data
        print('Message from server:', data)
        #'Hello, server!'
        #sio.disconnect()
    
    return 'Hello, Client!'

text = ""

def main_3(text):

    if text == "":
        pass
    else:
        #'Hello, server!'
        sio.emit('message_from_client', text)
    
    return text


def main_4():

    @sio.event
    def disconnect():
        print('Disconnected from server')

print(main())