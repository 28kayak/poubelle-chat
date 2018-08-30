import os
import sys
from flask import Flask, request, abort

from linebot import ( LineBotApi, WebhookHandler )

from linebot.exceptions import ( InvalidSignatureError )

from linebot.models import( MessageEvent, TextMessage, TextSendMessage )

app = Flask(__name__)


channel_access_token = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
channel_secret = os.environ['LINE_CHANNEL_SECRETE']

if channel_secret is None:
    print("Specify line-channel secret as environmental variable")
    sys.exit(1)
if channel_access_token is None:
    print("Specify Line-Channel-Access-Token as environmental variable")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/")
def hello_world():
    return "Hello World!!"


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    print(request.headers)
    signature = request.headers['X-Line-Signature']
    print("signature " + signature)

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
        #TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    #app.run()
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0',
            port=port)
    print("app is running")