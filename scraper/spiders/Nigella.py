from scrapy.spiders import SitemapSpider
from scraper.spiders.Base import RecipeMixin


class BBCGoodFoodSpider(SitemapSpider, RecipeMixin):
    '''
    Nigella doesn't use the ld+json tagging, so have to use xpath to parse out the fields manually
    '''
    name = 'Nigella'
    allowed_domains = ['www.nigella.com']
    sitemap_urls = ['https://www.nigella.com/sitemap.xml']

    sitemap_rules = [
        ('/recipes/', 'parse'),
    ]

    def get_kernel(self, response):
        section = response.xpath('//main[@itemtype]')
        if section:
            data = {'@type': section.xpath('@itemtype').get()}

            ingredients = []
            for p in section.xpath('//*[@itemprop]'):
                itemprop = p.xpath('@itemprop').get()
                if p.xpath('@content').get():
                    data[itemprop] = p.xpath('@content').get()

                elif p.xpath('@src').get():
                    data[itemprop] = response.urljoin(
                        p.xpath('@src').get()
                    )

                elif itemprop == 'recipeIngredient':
                    ingredients.append(
                        p.xpath("text()").get()
                    )
                    data[itemprop] = ingredients
                else:
                    data[itemprop] = p.xpath("text()").extract()

            return data, self.get_checksum(section.get())

        else:
            return None, None