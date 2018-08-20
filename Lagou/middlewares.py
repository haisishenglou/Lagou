# -*- coding: utf-8 -*-

import random

from Lagou.settings import USER_AGENT_LIST


class RandomRefererMiddleware(object):
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_LIST)
        request.headers['User-Agent'] = user_agent
        # request.headers['Referer'] = 'https://www.lagou.com/jobs/list_python?city=%E6%B7%B1%E5%9C%B3'
        # print("--" * 30)
        # print(request.headers)


