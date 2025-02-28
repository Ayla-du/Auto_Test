# 你想要怎样的生活
# 开发时间：2025/2/21 23:09

from api.api_url1.goods_detail import shopcarts, userfavs, cancelfavs, goods_detail
from component.request_untils import process_response


class Test_good_center():
    def shopcarts_api(self, data, token):
        response = shopcarts(data, token)
        process_response(response)
        return response.json()

    def userfavs_api(self, data, token):
        response = userfavs(data, token)
        process_response(response)
        return response.json()

    def cancelfavs_api(self, data, token):
        response = cancelfavs(data, token)
        process_response(response)
        return response

    def goods_detail_api(self, data, token):
        response = goods_detail(data, token)
        process_response(response)
        return response.json()