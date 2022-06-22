from scrapy.spiders import SitemapSpider
from scraper.spiders.Base import RecipeMixin


class BBCGoodFoodSpider(SitemapSpider, RecipeMixin):
    name = 'FattoInCasaDaBenedetta'
    allowed_domains = ['www.fattoincasadabenedetta.it']
    sitemap_urls = ['https://www.fattoincasadabenedetta.it/sitemap.xml']

    sitemap_rules = [
        ('/ricetta/', 'parse'),
    ]
