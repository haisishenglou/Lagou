# -*- coding: utf-8 -*-
import json

import scrapy
import time

from Lagou.items import LagouItem


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false'
    forset = 1
    def start_requests(self):
        headers = {
            'Referer': 'https://www.lagou.com/jobs/list_python?city=%E6%B7%B1%E5%9C%B3'
        }

        for i in range(1, 31):

            yield scrapy.FormRequest(
                url=self.start_urls,
                headers=headers,
                formdata={'first': 'true', 'pn': str(i), 'kd': 'python'},
                callback=self.parse,
                dont_filter=True
            )

    def parse(self, response):
        item = LagouItem()
        json_dic = json.loads(response.body)
        # print(json_dic)
        data_list = json_dic['content']['positionResult']['result']
        for data in data_list:
            item['position'] = data['positionName']
            item['company'] = data['companyFullName']
            item['createTime'] = data['createTime']
            yield item









