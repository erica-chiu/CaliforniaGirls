import wolfram

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
import urllib

# Account SID and Auth Token from www.twilio.com/console
client = Client('ACb324166cd2206250cb89a3b6b5631739', '5721a5e0622b1ef9ac514a1819fe2436')
app = Flask(__name__)

@app.route('/')
def index():
    print('Index')
    return 'Hello, world!'

# A route to respond to SMS messages and kick off a phone call.
@app.route('/sms', methods=['POST', 'GET'])
def sms():
    # Grab the question from the body of the text message.
    question = urllib.parse.quote(request.form['Body'])
    print('question: {}'.format(question))
    # Grab the relevant phone numbers.
    from_number = request.form['From']
    to_number = request.form['To']
    print('from: {} to: {}'.format(from_number, to_number))
    answer = wolfram.get_answer(question)
    print('answer: {}'.format(answer))
    response = MessagingResponse()
    response.message(answer)

    return str(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)