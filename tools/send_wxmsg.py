import requests
from tools import logger
from tools.env import wx_key,wx_url,wx_people
def send_wx_notification(content):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'X-API-Key': wx_key,
        'Content-Type': 'application/json;charset=UTF-8',
    }
    json_data = {
        'target': wx_people,
        "type": "TEXT",
        "content": f"吾爱破解 || {content}\n\n来自: 吾爱破解签到助手"
    }
    try:
        resp = requests.post(wx_url, headers=headers, json=json_data)
        if resp.status_code == 200:
            logger.info("微信通知发送成功")
        else:
            logger.error(f"微信通知失败: {resp.text}")
    except Exception as e:
        logger.error(f"微信通知异常: {e}")