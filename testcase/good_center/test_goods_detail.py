# 你想要怎样的生活
# 开发时间：2025/2/20 14:02
import allure
import pytest

from api.api.good_scnter_api import Test_good_center
from component.read_file import base_data


@allure.epic('商品管理')
@allure.feature('商品详情页')
class Test_goods_detail():
    @allure.story('查看商品详情')
    @allure.severity('blocker')
    @pytest.mark.parametrize('data', base_data.read_data('good_data.yaml')['goods_detail'])
    def test_goods_detail(self, data, login_fixture, fun):
        token = login_fixture
        with allure.step('请求查看商品详情接口'):
            result = Test_good_center().goods_detail_api(data, token)
        with allure.step('结果数据断言'):
            assert result['id'] == 55
            assert result['name'] == '帝王蟹'

    @allure.story('添加商品到购物车')
    @allure.severity('blocker')
    @pytest.mark.parametrize('data', base_data.read_data('good_data.yaml')['good'])
    def test_add_shopcarts(self, data, login_fixture, fun):
        token = login_fixture
        with allure.step('请求购物车接口'):
            result = Test_good_center().shopcarts_api(data, token)
        with allure.step('结果数据断言'):
            assert result['nums'] != ''
            assert result['goods'] == 28

    @allure.story('收藏商品')
    @allure.severity('blocker')
    @pytest.mark.parametrize('data', base_data.read_data('good_data.yaml')['favs_goods'])
    def test_add_userfav(self, data, login_fixture, fun):
        token = login_fixture
        with allure.step('请求商品收藏接口'):
            result = Test_good_center().userfavs_api(data, token)
        with allure.step('结果数据断言'):
            assert result['goods'] == 7

    @allure.story('取消收藏商品')
    @allure.severity('blocker')
    @pytest.mark.parametrize('data', base_data.read_data('good_data.yaml')['favs_goods'])
    def test_cancel_userfav(self, data, login_fixture, fun):
        token = login_fixture
        with allure.step('请求取消商品收藏接口'):
            result = Test_good_center().cancelfavs_api(data, token)
        with allure.step('结果数据断言'):
            assert result.status_code == 204, "取消收藏商品成功,返回结果为204"
