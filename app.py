# from flask import Flask, jsonify
# import random

# app = Flask(__name__)

# @app.route('/get_data', methods=['GET'])
# def get_data():
#     data = {
#         'temperature': random.uniform(20.0, 30.0),
#         'pressure': random.uniform(1.0, 2.0)
#     }
#     return jsonify(data)

# if __name__ == "__main__":
#     app.run(host='localhost', port=5000)

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'  # Clave secreta para SocketIO
socketio = SocketIO(app)
messages= []

@app.route('/')
def index():
    #print("print ",messages)
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('initial_messages', messages)

@socketio.on('message_from_client')
def handle_message(message):
    print('Received message from client:', message)
    messages.append(message)
    response = {'status': 'OK'}
    emit('message_from_server', response)
    emit('new_message', message, broadcast=True)  # Enviar el mensaje a todos los clientes conectados

if __name__ == '__main__':
    socketio.run(app, host='localhost', port=5000, debug=True)