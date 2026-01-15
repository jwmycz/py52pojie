from proxy.pool import CheckProxyPool,logger
from tools.env import proxy,proxy_url
def use_pro():
    if proxy:
        try:
            check = CheckProxyPool(proxy_url)
            trueproxy=check.trueproxy()
            logger.debug(trueproxy)
        except Exception as e:
            logger.debug(e)
            trueproxy=False
        return trueproxy