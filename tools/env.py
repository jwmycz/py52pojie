from tools.tools import read_env,read_cookies

env=read_env()
proxy=env['proxy']
proxy_url=env['proxy_url']
ck_data=env['ck_data']
wechat_url=env['wechat_url']
cron_expression=env['cron_expression']
wechat_url_open=env['wechat_url_open']
dingding_url=env['dingding_url']
dingding_url_open=env['dingding_url_open']
cookies=read_cookies(ck_data)