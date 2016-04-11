# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as BS
from scrapy import Spider
from scrapy.selector import Selector
import re


class pubmedSpider(Spider):
    name = "pubmed"
    allowed_domains = ["http://www.ncbi.nlm.nih.gov/"]

    def __init__(self, *args, **kwargs):
        super(pubmedSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('start_url')]

    def parse(self, response):
        link = response.url
        # meta tag includes authors' information.
        meta = response.css('head').css('meta')
        aid_list = [aid for aid in meta.extract() if 'author' in aid]
        raw_text = self.extract_text_from_response(response.xpath("//*[contains(@id, '__p')]").extract())
        abstract_text = self.extract_text_from_response(response.xpath("//*[contains(@id, 'abstract')]").extract())

        yield {
            'id': self.extract_ids(link),
            'title': self.extract_title(response.css('title').extract()),
            'link': link,
            'authors': self.extract_authors_from_meta(aid_list),
            'raw_text': raw_text,
            'abstract_text': abstract_text
        }

    def extract_ids(self, url):
        return re.sub(r'\D', r'', url)

    def extract_title(self, response_list):
        response_string = ''.join(response_list)
        marked_up_string = BS(response_string, 'lxml')
        clean_string = marked_up_string.get_text()
        return str(clean_string)

    def extract_authors_from_meta(self, response_list):
        author_list = []
        for response in response_list:
            bs = BS(response, 'lxml')
            author = bs.findAll('meta')[0].get('content')
            author_list.append(author)
        return author_list

    def extract_text_from_response(self, raw_response):
        return BS('\n\n'.join(raw_response), 'lxml').get_text()
