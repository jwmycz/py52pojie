import os
import re
import sys
import json
import execjs
from . import logger

def resource_path(relative_path: str) -> str:
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

    return os.path.join(base_path, relative_path)

def read_cookies(file_name: str) -> dict:
    ck = {}

    path = resource_path(file_name)

    if not os.path.exists(path):
        raise FileNotFoundError(f'Cookie 文件不存在: {path}')

    with open(path, 'r', encoding='utf-8') as f:
        cookie_list = json.load(f)

    for item in cookie_list:
        name = item.get('name')
        value = item.get('value')
        if name is not None:
            ck[name] = value

    return ck


def read_env() -> dict:
    env_path = resource_path(os.path.join('env', 'env.json'))

    if not os.path.exists(env_path):
        raise FileNotFoundError(f'env.json 不存在: {env_path}')

    with open(env_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def match_res(data):
    pattern = r"LZ='([^']+)'.*?LJ='([^']+)'.*?LE='([^']+)'"

    match = re.search(pattern, data, re.S)
    if match:
        LZ, LJ, LE = match.groups()
        logger.debug(f'提取参数：LZ--》{LZ}，LJ--》{LJ}，LE--》{LE}')
        return [LZ, LJ, LE]
def get_js():
    js_file = resource_path(os.path.join('js', 'waf.js'))

    if not os.path.exists(js_file):
        raise FileNotFoundError(f"文件不存在: {js_file}")

    with open(js_file, 'r', encoding='utf-8') as f:
        js_code = f.read()
    return js_code
def call_js(LZ, LJ, LE):
    try:
        ctx = execjs.compile(get_js())
        data = ctx.call('qd', str(LZ), str(LJ), str(LE))
        logger.debug(f'waf参数：{data}')
        return data
    except Exception as e:
        pass



if __name__ == '__main__':
    data=get_js()
    print(data)