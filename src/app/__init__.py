from flask import Flask
from flask import request, jsonify
from service.messageService import MessageService
import json

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/v1/ds/message/', methods=['POST'])
def handle_message():
    message = request.json.get('message')
    result = MessageService().process_message(message)
    return jsonify(str(result))

@app.route("/", methods=['GET'])
def handle_get():
    print("Hello World")
if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)