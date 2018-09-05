import socket

from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response

VW_HOST = '127.0.0.1'
VW_PORT = 26542

app = Flask(__name__)

# Horrible, change this logic
def send(req):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((VW_HOST, VW_PORT))
    s.sendall(req)
    buffer = ''
    while True:
        buffer += s.recv(1).decode('utf-8')
        if '\n' in buffer:
            msg, sep, _ = buffer.partition('\n')
            s.shutdown(socket.SHUT_WR)
            s.close()
            return float(msg)


@app.route('/train', methods=['POST'])
def train():
    body = request.get_json()
    req = '{0} | {1}\n'.format(
        body['response'],
        body['context']
    ).encode()
    try:
        return jsonify({'prediction': send(req)})
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)


@app.route('/save', methods=['POST'])
def save():
    body = request.get_json()
    filename = body['filename']
    req = 'save_{0}\n'.format(filename).encode()
    send(req)
    return jsonify({'model file': filename})

