from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage

import configparser

import urllib
import re
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
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def pixabay_isch(event):
    
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        try:
            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(
                    type="image",
                    original_content_url="https://github.com/chongyi0717/wireless_project/blob/master/distribution.png",
                    preview_image_url="https://github.com/chongyi0717/wireless_project/blob/master/distribution.png"
                )
            )
        # 如果找不到圖，就學你說話
        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=event.message.text)
            )
            pass

if __name__ == "__main__":
    app.run()