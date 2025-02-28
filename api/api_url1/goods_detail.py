# 你想要怎样的生活
# 开发时间：2025/2/19 16:50
from common.requests import request

# url管理
def login(data):
    return request('/login/', 'POST', data=data)

def shopcarts(data, token):
    return request('/shopcarts/', 'POST', data=data, headers={'authorization': 'JWT ' + token})

def userfavs(data, token):
    return request('/userfavs/', 'POST', data=data, headers={'authorization': 'JWT ' + token})

def cancelfavs(data, token):
    return request('/userfavs/' + str(data['goods']) + '/', 'DELETE', params=None, headers={'authorization': 'JWT ' + token})

def goods_detail(data, token):
    return request('/goods/' + str(data['goods']) + '/', 'GET', params=data, headers={'authorization': 'JWT ' + token})