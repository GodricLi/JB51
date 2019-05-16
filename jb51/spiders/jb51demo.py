# -*- coding: utf-8 -*-
import scrapy


class Jb51demoSpider(scrapy.Spider):
    name = 'jb51demo'
    # allowed_domains = ['https://i.51job.com/userset/my_51job.php']
    start_urls = ['https://login.51job.com/login.php?lang=c']

    def start_requests(self):
        print('start...')
        data = {
            'lang': 'c',
            'action': 'save',
            'from_domain': 'i',
            'loginname': '635434705@qq.com',
            'password': '635434705qaz',
            'verifycode: ': ''
        }
        for url in self.start_urls:
            yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse)

    def paser_51jb(self, response):
        with open('./my_51jb.html', 'w', encoding='gbk') as f:
            f.write(response.text)
        print('end...')

    def parse(self, response):
        with open('./login_51.html', 'w', encoding='gbk') as f:
            f.write(response.text)

        url = 'https://i.51job.com/userset/my_51job.php '
        yield scrapy.Request(url=url, callback=self.paser_51jb)
