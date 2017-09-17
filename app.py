import wolfram
import my_keys #delete this in your own code

from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse, Message
from twilio.rest import Client
import urllib

#replace my_keys.get_key(foo) with your twilio sid and auth
client = Client(my_keys.get_key('twilio sid'), my_keys.get_key('twilio auth'))
app = Flask(__name__)

@app.route('/')
def index():
    #return 'Hello, world!'
    return render_template("mainpage.html")

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