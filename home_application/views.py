# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import http.client
import json
from blueking.component.shortcuts import get_client_by_request
conn = http.client.HTTPSConnection("bkapi.ce.bktencent.com")

# 开发框架中通过中间件默认是需要登录态的，如有不需要登录的，可添加装饰器login_exempt
# 装饰器引入 from blueapps.account.decorators import login_exempt
def home(request):
    """
    首页
    """
    test_txt = "进入了单点调试"
    print(test_txt)
    return render(request, "home_application/index_home.html")


def dev_guide(request):
    """
    开发指引
    """
    return render(request, "home_application/dev_guide.html")


def contact(request):
    """
    联系页
    """
    return render(request, "home_application/contact.html")


def search_business(request):
    """
    查询业务列表
    """

    # 从环境配置获取APP信息，从request获取当前用户信息
    client = get_client_by_request(request)
    kwargs = {
        "fields": [
            "bk_biz_id",
            "bk_biz_name"
        ],
        "page": {
            "start": 0,
            "limit": 10,
            "sort": ""
        }
    }
    result = client.cc.search_business(kwargs)
    return JsonResponse(result)
    # return HttpResponse(json.dumps(data_json, ensure_ascii=False), content_type="application/json;charset=utf-8")
