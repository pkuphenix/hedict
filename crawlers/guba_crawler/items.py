# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GubaShare(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    share_id = scrapy.Field()
    share_name = scrapy.Field()
    share_href = scrapy.Field()

class GubaTopic(scrapy.Item):
	topic_id = scrapy.Field()
	topic_time = scrapy.Field()
	topic_author = scrapy.Field()
	topic_title = scrapy.Field()
	topic_content = scrapy.Field()
	topic_reply_count = scrapy.Field()
	topic_view_count = scrapy.Field()
	share_id = scrapy.Field()
	share_name = scrapy.Field()