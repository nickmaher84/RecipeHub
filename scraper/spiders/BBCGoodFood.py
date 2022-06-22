from scrapy.spiders import SitemapSpider
from scraper.spiders.Base import RecipeMixin


class BBCGoodFoodSpider(SitemapSpider, RecipeMixin):
    name = 'BBCGoodFood'
    allowed_domains = ['www.bbcgoodfood.com']
    sitemap_urls = ['https://www.bbcgoodfood.com/sitemap.xml']

    sitemap_rules = [
        ('/recipes/collection/', 'ignore'),
        ('/recipes/category/', 'ignore'),
        ('/recipes/', 'parse'),
    ]
    
    def ignore(self, response):
        pass
