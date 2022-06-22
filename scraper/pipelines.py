from scraper.database import engine, metadata, raw_table
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class RecipePipeline:
    def __init__(self):
        self.engine = engine
        self.metadata = metadata
        self.table = raw_table
        
        self.table.create(checkfirst=True)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.engine.execute(
            self.table.insert().values(
                adapter.asdict()
            )
        )
        return item
