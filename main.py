from scrapy import Spider
from scrapy.http.response.html import HtmlResponse


class GitHubPinsSpider(Spider):
    name = 'github.pins'
    start_urls = ['https://github.com/brunodavi']

    def parse(self, response: HtmlResponse):
        for repo in response.css('span.repo'):
            yield { 'repoName': repo.attrib['title'] }