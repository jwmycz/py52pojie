import requests
from . import logger
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
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
def send_dingtalk_notification(url,content):
    payload = {
        "msgtype": "text",
        "text": {"content": f"吾爱破解 || {content}\n\n来自: 吾爱破解签到助手"}
    }
    try:
        resp = requests.post(url, headers={'Content-Type': 'application/json'}, json=payload)
        if resp.status_code == 200:
            logger.info("钉钉通知发送成功")
        else:
            logger.error(f"钉钉通知失败: {resp.text}")
    except Exception as e:
        logger.error(f"钉钉通知异常: {e}")