from scrapy.spiders import SitemapSpider
from scraper.spiders.Base import RecipeMixin


class BBCGoodFoodSpider(SitemapSpider, RecipeMixin):
    '''
    Has a rate limit on the server, so need to add in a time delay else we start getting 429 (Too Many Requests).
    Keeping it to less than one request per second seems to keep it happy.
    '''
    name = 'JamieOliver'
    allowed_domains = ['www.jamieoliver.com']
    sitemap_urls = ['https://www.jamieoliver.com/recipes.xml']
    download_delay = 1.0

    sitemap_rules = [
        ('/recipes/', 'parse'),
    ]
