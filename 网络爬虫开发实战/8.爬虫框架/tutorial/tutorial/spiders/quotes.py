import scrapy

from tutorial.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    # 这个是项目的名字
    name = 'quotes'
    # 允许爬取的域名
    allowed_domains = ['quotes.toscrape.com']
    # 初始请求url
    start_urls = ['http://quotes.toscrape.com/']

    # 这里是解析函数
    def parse(self, response):
        # 使用css选择器来解析
        quotes = response.css('.quote')
        for quote in quotes:
            # 获取一个item，然后分别使用选择器获取到对应的内容赋值到item里面去
            item = QuoteItem()
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()
            yield item

        # 获取下一个链接的地址并请求
        next = response.css('.pager .next a::attr(href)').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)


