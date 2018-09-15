import os
import sys
import requests
from datetime import datetime
from flask import Flask, request, abort

from linebot import ( LineBotApi, WebhookHandler )

from linebot.exceptions import ( InvalidSignatureError )

from linebot.models import( MessageEvent, TextMessage, TextSendMessage )

app = Flask(__name__)


#channel_access_token = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
#channel_secret = os.environ['LINE_CHANNEL_SECRETE']

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

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
    #return app.send_static_file('./index.html')
    return "Hello world"



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

# push notification
@app.route('/push_trash', methods=['GET'])
def push_trash():
    return_text = "ーー今日 捨てられるゴミーー\n"
    # 0 : Mon
    # 1 : Tue
    # 2 : Web
    # 3 : Thu
    # 4 : Fri
    # 5 : Sat
    # 6 : Sun

    trash_schedule = {
        0: "燃えないゴミ　・　有害危険ゴミ",
        1: "燃えるゴミ",
        2: "資源物１類　 ビン・カン・ペットボトル",
        3: "捨てられるゴミはありません",
        4: "燃えるゴミ",
        5: "捨てられるゴミはありません",
        6: "資源回収（資源２類）古着・新聞紙・雑誌"
    }
    weekday = datetime.now().weekday()
    return_text += trash_schedule[weekday]
    to = "Ua21ed0b7a6399fad17ba2adfd9efaa03"

    line_bot_api.push_message(to, TextSendMessage(text=return_text))

    return 'OK'




@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):



    trash_schedule = {
        0: "燃えないゴミ　・　有害危険ゴミ",
        1: "燃えるゴミ",
        2: "資源物１類　 ビン・カン・ペットボトル",
        3: "捨てられるゴミはありません",
        4: "燃えるゴミ",
        5: "捨てられるゴミはありません",
        6: "資源回収（資源２類）古着・新聞紙・雑誌"
    }
    weekday = datetime.now().weekday()
    if event.message.text == "今日":
        text = trash_schedule[weekday]
    elif event.message.text == "明日":
        text = trash_schedule[weekday + 1]
    elif event.message.text == "明後日":
        text = trash_schedule[weekday + 2]
    else:
        trash_name = event.message.text
        query = 'trash_name:' + trash_name
        params = (
            ('indent', 'on'),
            ('q', query),
            ('wt', 'json'),
        )

        # get request to solr
        response = requests.get('http://4d8d496e.ngrok.io/solr/trash/select', params=params)
        # Original curl command
        # curl http://localhost:8983/solr/trash/select?indent=on&q=trash_name:雨戸&wt=json
        # response = requests.get('http://localhost:8983/solr/trash/select?indent=on&q=trash_name:雨戸&wt=json')

        if response.status_code == 200:
            search_result = response.json()
            # print wjdata['data']['current_condition'][0]['temp_C']
            print(search_result['response']['doc']['trash_name'])
            text = "分別カテゴリー　:" + search_result['category'] + "\n" + "捨てる方法　:" + search_result['method']




    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text))
        #TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    #app.run()
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0',
            port=port)
    print("app is running")
