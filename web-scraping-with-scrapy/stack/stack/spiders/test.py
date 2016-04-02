# -*- coding: utf-8 -*-

from scrapy import Spider
from scrapy.selector import Selector
from stack.items import StackItem


class TestSpider(Spider):
    name = 'test'
    allowed_domains = ['test.com']

    def __init__(self, *args, **kwargs):
        super(TestSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('start_url')]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            yield item
