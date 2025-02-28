# 你想要怎样的生活
# 开发时间：2025/2/19 17:12
import json
from component.log_untils import logger

# 检查响应状态码,打印接口返回内容
def process_response(response):
    if response.status_code == 200 or response.status_code == 201:
        logger.info('接口返回内容>>>:' + json.dumps(response.json(), ensure_ascii=False))

    elif response.status_code == 204:
        logger.info('状态码为204,无返回结果')

    else:
        logger.info('状态码非200/201,请检查')
