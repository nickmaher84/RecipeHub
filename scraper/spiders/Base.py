from scrapy.spiders import Spider
from scraper.items import RecipeItem
from hashlib import md5
from pendulum import now
import json


class RecipeMixin(Spider):

    def parse(self, response, **kwargs):
        data, checksum = self.get_kernel(response)

        item = RecipeItem(
            url=response.url,
            json=data,
            checksum=checksum,
            language=self.get_language(response),
            spider=self.name,
            timestamp=now(),
        )

        if checksum:
            yield item

    def get_kernel(self, response):
        for script in response.xpath('//script[@type="application/ld+json"]//text()').getall():
            data = json.loads(script)

            if data.get('@type') == 'Recipe':
                return data, self.get_checksum(script)

        else:
            return None, None

    def get_language(self, response):
        return response.xpath('/html/@lang').get()

    def get_checksum(self, text):
        return md5(text.encode('utf-8')).hexdigest()
