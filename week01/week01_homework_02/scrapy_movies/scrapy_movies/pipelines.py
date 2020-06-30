# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas

class ScrapyMoviesPipeline(object):
    def process_item(self, item, spider):
        data = [item['movie_name'], item['movie_type'], item['movie_date']]
        movie_df = pandas.DataFrame(columns=data)
        movie_df.to_csv('top10_movies.csv', mode='a', encoding='GBK', index=False, header=True)
        return item
