from chatbase import Message
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import random
app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('ToflcXGuE9cm5WmDysvWWVPSSM2KCRe8k7bVP5EjF12yuXqqBSorgzDsEbxrSFp3ZL5KCTuZGXFyYvHht1sWd2AZMrbyYB1Po+yjWgDjSzBrBAkB43RDeuk6FhH12Kvv1s1YNF3QfVv1TBZAcjG6XwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5186fcb8bf05dc424db1e061775f4239')


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    #app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

def movie():
    target_url = 'https://movies.yahoo.com.tw/'
    print('Start parsing movie ...')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')   
    content = ""
    for index, data in enumerate(soup.select('div.movielist_info h1 a')):
        if index == 20:
            return content
        print("data：")
        print(index)
        print(data)        
        title = data.text
        link =  data['href']
        content += '{}\n{}\n'.format(title, link)
    return content

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    #print(type(msg))
    msg = msg.encode('utf-8')
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

# 學你說話
# stage=["type","location"]
# current_stage=0
# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     msg=event.message.text
#     msg=msg.encode("utf-8")
#     if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
#         if event.message.text == "文字":
#             line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))
#         elif event.message.text == "貼圖":
#             line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id=random.randint(1,10), sticker_id=random.randint(1,10)))

if __name__ == "__main__":
    app.run()