import requests
from tools import logger,headers

def send_wechat_notification(url,content):
    payload = {
        "msgtype": "text",
        "text": {"content": f"吾爱破解 || {content}\n\n来自: 吾爱破解签到助手"}
    }
    try:
        resp = requests.post(url, headers=headers, json=payload)
        if resp.status_code == 200:
            logger.info("企业微信通知发送成功")
        else:
            logger.error(f"企业微信通知失败: {resp.text}")
    except Exception as e:
        logger.error(f"企业微信通知异常: {e}")