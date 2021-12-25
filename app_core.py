from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import configparser
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
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    #print(type(msg))
    msg = msg.encode('utf-8')
    flag=False
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        if event.message.text == "選單":
            flag=True
            line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Menu',
                            template=ButtonsTemplate(
                                title='Menu',
                                text='今天想吃什麼樣的餐點呢？',
                                actions=[
                                    MessageTemplateAction(
                                        label='中式',
                                        text='中式'
                                    ),
                                    MessageTemplateAction(
                                        label='台式',
                                        text='台式'
                                    ),
                                    MessageTemplateAction(
                                        label='美式',
                                        text='美式'
                                    ),
                                    MessageTemplateAction(
                                        label='越式',
                                        text='越式'
                                    )
                                ]
                            )
                        )
                    )
        elif(event.message.text=="中式"):
            flag=True
            line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TemplateSendMessage(
                            alt_text='Menu',
                            template=ButtonsTemplate(
                                title='Menu',
                                text='今天想吃什麼樣的餐點呢？',
                                actions=[
                                    MessageTemplateAction(
                                        label='中式',
                                        text='中式'
                                    ),
                                    MessageTemplateAction(
                                        label='台式',
                                        text='台式'
                                    ),
                                    MessageTemplateAction(
                                        label='美式',
                                        text='美式'
                                    ),
                                    MessageTemplateAction(
                                        label='越式',
                                        text='越式'
                                    )
                                ]
                            )
                        )
                    )
        if(flag!=True):
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="抱歉，您輸入的文字還不能對應當前的stage"))

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
    current_stage="nothing"
    app.run()