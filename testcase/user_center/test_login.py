# 你想要怎样的生活
# 开发时间：2025/2/19 15:05
import allure
import pytest

from api.api.login_api import login_api
from component.read_file import base_data


@allure.epic('用户中心模块')
@allure.feature('用户登录')
class Test_login():
    @allure.story('正常登录')
    @allure.severity('blocker')
    @pytest.mark.parametrize('data', base_data.read_data('login_data.yaml')['user'])
    def test_login(self, data, fun):
        with allure.step('请求登录接口'):
            result = login_api(data)
        with allure.step('结果数据断言'):
            assert len(result['token']) != 0