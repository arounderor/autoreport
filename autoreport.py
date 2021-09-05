import requests
import re
import time
import os
###########用户需要更改的部分###############
your_name = os.environ["YOUR_NAME"]
#your_name = "whz19376238"
your_pwd = os.environ["YOUR_PWD"]
#your_pwd = "whz08070011"
#wechat_key = os.environ["WECHAT_KEY"]
form_data = os.environ["FORM_DATA"]
###########用户需要更改的部分###############

def buaaLogin(user_name, password):
    print("统一认证登录")

    postUrl = "https://app.buaa.edu.cn/uc/wap/login/check"
    postData = {
        "username": user_name,
        "password": password,
    }
    responseRes = requests.post(postUrl, data=postData)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    # print(f"statusCode = {responseRes.status_code}")
    print(f"text = {responseRes.text}")
    return responseRes


def fillForm(res):
    s = requests.session()
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://app.buaa.edu.cn/site/buaaStudentNcov/index',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': res.headers['set-cookie']
    }
    r = s.post('https://app.buaa.edu.cn/buaaxsncov/wap/default/save', data=form_data, headers=headers)
    return r


def main_handler():
    result = fillForm(buaaLogin(your_name, your_pwd))
    print(result.headers)
    return("DONE")
main_handler()
