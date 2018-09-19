from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)

ACCESS_TOKEN = "EAADylOCdiqkBAEwQvU1xzaBil1ZCGOFjVNBUORZAmGi7rd6azYVVUOyuvmjluIjZCBlrfPAeZClor0SZCH9YdZAaaioYmQsmJaIJeUlgNxWkwRDr1IHuUvXvD9fGwf05ZAVBmLIn4po4cpTMbveZAjMpyBLTTv7wBZA5hheZC1uqkaUQZDZD"
VERIFY_TOKEN = "jednadvatri"
bot = Bot(ACCESS_TOKEN)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'

    if request.method == 'POST':
        output = request.get_json()
        print(output)
        for event in output['entry']:
            #messaging = event['messaging']
            for text in event['standby']:
                zprava = text['message']['text']
                sender = text['sender']['id']
                print(zprava, sender)


            '''for x in text['message']:
                if x.get('message'):
                    recipient_id = x['sender']['id']
                    if x['message'].get('text'):
                        message = x['message']['text']
                        bot.send_text_message(recipient_id, message)
                    if x['message'].get('attachments'):
                        for att in x['message'].get('attachments'):
                            bot.send_attachment_url(recipient_id, att['type'], att['payload']['url'])
                else:
                    pass'''
        return "Success", 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)
