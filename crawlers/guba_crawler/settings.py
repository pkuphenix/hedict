# -*- coding: utf-8 -*-

# Scrapy settings for guba_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#


BOT_NAME = 'guba_crawler'

SPIDER_MODULES = ['guba_crawler.spiders']
NEWSPIDER_MODULE = 'guba_crawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'guba_crawler (+http://www.yourdomain.com)'

#FEED_URI = '%(name)s_%(time)s.json'
#FEED_FORMAT = 'json'

LOG_LEVEL = 'INFO'
ITEM_PIPELINES = ['guba_crawler.pipelines.MongoDBPipeline']

