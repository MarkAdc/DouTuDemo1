# # -*- coding: utf-8 -*-
import random


# 函数的返回值是一个随机User-Agent
def get_ua():
    first_num = random.randint(55, 62)
    third_num = random.randint(0, 3200)
    fourth_num = random.randint(0, 140)
    os_type = [
        '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
        '(Macintosh; Intel Mac OS X 10_12_6)'
    ]
    chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

    ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
                   '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
                  )
    return ua


# 设置请求头User_Agent
class RandomUa:
    def process_request(self, request, spider):
        # print('随机请求头')
        request.headers['User-Agent'] = get_ua()

        # print('随机请求头设置成功')

    # def process_response(self, request, response, spider):
    #     print(request.headers['User-Agent'])
    #     print()
    #     print()
    #     return response


# 输出请求头User-Agent
class PrintUa:
    def process_response(self, request, response, spider):
        print('当前请求头', request.headers['User-Agent'])
        # print('当前cookie', request.headers['Cookie'])
        return response


# 使用代理
class ProxyMiddleware(object):
    def process_request(self, request, spider):
        pass
        # print('代理')
        # request.meta["proxy"] = {"https":"https://116.209.58.225:99991"}
        # print('代理设置成功')