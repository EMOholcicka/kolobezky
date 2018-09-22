import os, sys
from flask import Flask, request
from pymessenger import Bot

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAEpbPk5JG0BAO8cx3qZCd9oRaeaUKWtjl3AaoZCVvVZCl1cO5GF6sGdRSZBRdbDI4gVZAUFfPVm7uZAPGuVR8Kc3n7H4DXBFsXzP2bbrmRwaCdqaZBqluzaufbAtqK9OwqYWzna8XGuAqOzycwHnwkNVQC9mai7sAjrRbkgYURPgZDZD"

bot = Bot(PAGE_ACCESS_TOKEN)


@app.route('/webhook', methods=['GET'])
def verify():
	# Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "5e495b826b8bbec66e6b33c735a34e11":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200


@app.route('/webhook', methods=['POST'])
def webhook():
	data = request.get_json()
	log(data)

	if data['object'] == 'page':
		for entry in data['entry']:
			for messaging_event in entry['messaging']:

				# IDs
				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					# Extracting text message
					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
					else:
						messaging_text = 'no text'

					response = None

					entity, value = wit_response(messaging_text)
					if entity == 'newstype':
						response = "Ok, I will send you the {} news".format(str(value))
					elif entity == 'location':
						response = "Ok, so you live in {0}. Here are top headlines from {0}".format(str(value))

					if response == None:
						response = "I have no idea what you are saying!"
						
					bot.send_text_message(sender_id, response)

	return "ok", 200


def log(message):
	print(message)
	sys.stdout.flush()


if __name__ == "__main__":
	app.run(debug = True, port = 80)
