# 你想要怎样的生活
# 开发时间：2025/2/19 15:23
import os

import pytest as pytest

from api.api.login_api import login_api
from component.log_untils import logger

# 方法级前置后置打印


@pytest.fixture()
def fun():
    logger.info('开始执行用例')
    yield
    logger.info('执行完毕~')

@pytest.fixture()
def login_fixture():
    if 'token' not in os.environ:
        result = login_api(data={'username': 15819749552, 'password': 123456})
        # token添加到环境变量
        os.environ['token'] = result['token']
        return result['token']
    else:
        return os.environ['token']



