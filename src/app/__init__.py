from flask import Flask
from flask import request, jsonify
from service.messageService import MessageService
import json
from kafka import KafkaProducer

app = Flask(__name__)
app.config.from_pyfile('config.py')
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda v:json.dumps(v).encode('utf-8'))

@app.route('/v1/ds/message/', methods=['POST'])
def handle_message():
    message = request.json.get('message')
    result = MessageService().process_message(message)
    serialized_result = result.json()

    #send serialized mssg to the Kafka Topic
    producer.send('expense', serialized_result)
    return jsonify(result)

@app.route("/", methods=['GET'])
def handle_get():
    print("Hello World")
if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)