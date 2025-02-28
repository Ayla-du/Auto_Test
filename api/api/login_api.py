# 你想要怎样的生活
# 开发时间：2025/2/19 15:15
from api.api_url1.goods_detail import login
from component.request_untils import process_response

# 执行接口请求
def login_api(data):
    response = login(data)
    process_response(response)
    return response.json()


