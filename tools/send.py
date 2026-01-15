from tools.send_dd import send_dingtalk_notification
from tools.send_wx import send_wechat_notification
from tools.env import *
def send(content):
    if wechat_url_open:
        send_wechat_notification(wechat_url, content)
    if dingding_url_open:
        send_dingtalk_notification(dingding_url, content)

