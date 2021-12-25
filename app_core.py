from __future__ import unicode_literals
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler,WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from fsm import TocMachine
app = Flask(__name__)


# machine = TocMachine(
#     states=["user", "state1", "state2"],
#     transitions=[
#         {
#             "trigger": "advance",
#             "source": "user",
#             "dest": "state1",
#             "conditions": "is_going_to_state1",
#         },
#         {
#             "trigger": "advance",
#             "source": "user",
#             "dest": "state2",
#             "conditions": "is_going_to_state2",
#         },
#         {"trigger": "go_back", "source": ["state1", "state2"], "dest": "user"},
#     ],
#     initial="user",
#     auto_transitions=False,
#     show_conditions=True,
# )

# LINE 聊天機器人的基本資料
channel_secret='5186fcb8bf05dc424db1e061775f4239'
channel_access_token='ToflcXGuE9cm5WmDysvWWVPSSM2KCRe8k7bVP5EjF12yuXqqBSorgzDsEbxrSFp3ZL5KCTuZGXFyYvHht1sWd2AZMrbyYB1Po+yjWgDjSzBrBAkB43RDeuk6FhH12Kvv1s1YNF3QfVv1TBZAcjG6XwdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(channel_access_token)
parser=WebhookParser(channel_secret)


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    # signature = request.headers['X-Line-Signature']

    # body = request.get_data(as_text=True)
    
    # app.logger.info("Request body: " + body)
    
    # try:
    #     events = parser.parse(body, signature)
    # except InvalidSignatureError:
    #     abort(400)
    # for event in events:
    #     if not isinstance(event, MessageEvent):
    #         continue
    #     if not isinstance(event.message, TextMessage):
    #         continue

    #     line_bot_api.reply_message(
    #         event.reply_token, TextSendMessage(text=event.message.text)
    #     )
    return 'OK'

@app.route("/webhook", methods=["POST"])
def webhook_handler():
    # signature = request.headers["X-Line-Signature"]
    # # get request body as text
    # body = request.get_data(as_text=True)
    # app.logger.info(f"Request body: {body}")

    # # parse webhook body
    # try:
    #     events = parser.parse(body, signature)
    # except InvalidSignatureError:
    #     abort(400)

    # # if event is MessageEvent and message is TextMessage, then echo text
    # for event in events:
    #     if not isinstance(event, MessageEvent):
    #         continue
    #     if not isinstance(event.message, TextMessage):
    #         continue
    #     if not isinstance(event.message.text, str):
    #         continue
    #     print(f"\nFSM STATE: {machine.state}")
    #     print(f"REQUEST BODY: \n{body}")
    #     response = machine.advance(event)
    #     if response == False:
    #         send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     msg = event.message.text
#     #print(type(msg))
#     msg = msg.encode('utf-8')
#     flag=False
#     if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
#         if event.message.text == "選單":
#             flag=True
#             line_bot_api.reply_message(  # 回復傳入的訊息文字
#                         event.reply_token,
#                         TemplateSendMessage(
#                             alt_text='Menu',
#                             template=ButtonsTemplate(
#                                 title='Menu',
#                                 text='今天想吃什麼樣的餐點呢？',
#                                 actions=[
#                                     MessageTemplateAction(
#                                         label='中式',
#                                         text='中式'
#                                     ),
#                                     MessageTemplateAction(
#                                         label='台式',
#                                         text='台式'
#                                     ),
#                                     MessageTemplateAction(
#                                         label='美式',
#                                         text='美式'
#                                     ),
#                                     MessageTemplateAction(
#                                         label='越式',
#                                         text='越式'
#                                     )
#                                 ]
#                             )
#                         )
#                     )
#         elif(event.message.text=="中式"):
#             flag=True
#             line_bot_api.reply_message(  # 回復傳入的訊息文字
#                         event.reply_token,
#                         TemplateSendMessage(
#                             alt_text='Menu',
#                             template=ButtonsTemplate(
#                                 title='Menu',
#                                 text='今天想吃什麼樣的餐點呢？',
#                                 actions=[
#                                     MessageTemplateAction(
#                                         label='中式',
#                                         text='中式'
#                                     ),
#                                     MessageTemplateAction(
#                                         label='台式',
#                                         text='台式'
#                                     ),
#                                     MessageTemplateAction(
#                                         label='美式',
#                                         text='美式'
#                                     ),
#                                     MessageTemplateAction(
#                                         label='越式',
#                                         text='越式'
#                                     ),
                                    
#                                 ]
#                             )
#                         )
#                     )
#         if(flag!=True):
#             line_bot_api.reply_message(event.reply_token,TextSendMessage(text="抱歉，您輸入的文字還不能對應當前的stage"))

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