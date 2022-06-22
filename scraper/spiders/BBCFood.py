from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scraper.spiders.Base import RecipeMixin


class BBCFoodSpider(CrawlSpider, RecipeMixin):
    name = 'BBCFood'
    allowed_domains = ['www.bbc.co.uk']
    start_urls = ['https://www.bbc.co.uk/food/recipes/a-z/']

    rules = [
        Rule(LinkExtractor(
            allow=(
                '/food/recipes/a-z',
                '/food/ingredients',
                '/food/cuisines',
                '/food/collections',
                '/food/occasions',
                '/food/seasons',
                '/food/techniques',
                '/food/chefs',
            )
        )),
        Rule(LinkExtractor(allow=r'/food/recipes/[a-z0-9_-]+\d+$'), callback='parse'),
    ]

    def parse(self, response, **kwargs):
        path = response.url.split('/')[-1]
        number = int(path.split('_')[-1])

        for item in super().parse(response, **kwargs):
            item['json'].update(number=number)

            yield item
