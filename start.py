import re
from lxml import etree
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from tools.tools import *
from tools.send_wx import send_wechat_notification

session=requests.Session()
job_defaults = {
    'coalesce': True,
    'misfire_grace_time': 1500,
}
scheduler = BlockingScheduler(timezone='Asia/Shanghai', job_defaults=job_defaults)
env=read_env()
proxy=env['proxy']
ck_data=env['ck_data']
wechat_url=env['wechat_url']
cookies=read_cookies(ck_data)


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Referer': 'https://www.52pojie.cn/',
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
session.headers.update(headers)
session.cookies.update(cookies)

def get_waf_data():
    params = {
        'mod': 'task',
        'do': 'apply',
        'id': '2',
        'referer': '//',
    }
    response = session.get('https://www.52pojie.cn/home.php', params=params, cookies=cookies, headers=headers)
    logger.debug(f'混淆响应：{response.text[:300]}')
    match=match_res(response.text)
    if match:
        LZ=match[0]
        LJ=match[1]
        LE =match[2]
        waf_data=call_js(str(LZ), str(LJ), str(LE))
        return waf_data
def bypass_waf():
    waf_data=get_waf_data()
    if waf_data:
        resp = session.post('https://www.52pojie.cn/waf_zw_verify', data=waf_data)
        logger.debug(f'防火墙响应：{resp.text[:300]}')
        if resp.text=='ok':
            return True
        else:
            return False
def check_in():
    if bypass_waf():
        session.headers.update({'Referer': 'https://www.52pojie.cn/home.php?mod=task&do=apply&id=2&referer=%2F'})
        response=session.get('https://www.52pojie.cn/home.php?mod=task&do=apply&id=2&referer=%2Fhome.php%3Fmod%3Dtask%26do%3Ddraw%26id%3D2%26referer%3Dhttps%253A%252F%252Fwww.52pojie.cn%252F.%252F%252F')
        logger.debug(f'签到响应：{response.text}')
        pt="//div[@id='messagetext']/p/text()"
        ctx=etree.HTML(response.text)
        data=ctx.xpath(pt)
        logger.info(data[0])
        send_wechat_notification(wechat_url,data[0])

def start():
    check_in()

def start_sch():

    scheduler.add_job(
        check_in,
        trigger='cron',
        name='吾爱破解论坛',
        hour=8,
        minute=0,
        second=0
    )
    scheduler.start()
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("请提供启动方式参数: start | sch")
        sys.exit(1)

    mode = sys.argv[1].lower()

    if mode == "start":
        start()
    elif mode == "sch":
        start_sch()
    else:
        print("无效参数，请使用: start | sch")