from scrapy.spiders import SitemapSpider
from scraper.spiders.Base import RecipeMixin


class BBCGoodFoodSpider(SitemapSpider, RecipeMixin):
    name = 'AllRecipes'
    allowed_domains = ['www.allrecipes.com']
    sitemap_urls = ['https://www.allrecipes.com/sitemap.xml']

    sitemap_rules = [
        ('/recipes/', 'parse'),
    ]

    def parse(self, response, **kwargs):
        path = response.url.split('/')[-2]
        number = int(path)

        for item in super().parse(response, **kwargs):
            item['json'].update(number=number)

            yield item
