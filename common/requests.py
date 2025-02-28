# 你想要怎样的生活
# 开发时间：2025/2/19 15:39
import os
import requests
from component.log_untils import logger
from component.read_file import base_data

api_root_url = base_data.read_ini()['host']['domain_name']

# 底层api请求,打印请求日志
def request(url, method,**kwargs,):
    logger.info('接口地址>>>>>:{}'.format(api_root_url + url))
    if method == 'GET':
        logger.info('接口参数>>>>>:{}'.format(kwargs['params']))
        return requests.get(api_root_url + url, **kwargs)

    elif method == 'POST':
        logger.info('接口参数>>>>>:{}'.format(kwargs['data']))
        return requests.post(api_root_url + url, **kwargs)

    elif method == 'DELETE':
        logger.info('接口参数>>>>>:{}'.format(kwargs['params']))
        return requests.delete(api_root_url + url, **kwargs)