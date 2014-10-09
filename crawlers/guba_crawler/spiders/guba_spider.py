# -*- coding: utf-8 -*-
import scrapy
import re, time
from datetime import datetime
from guba_crawler.items import GubaShare, GubaTopic


class GubaSpider(scrapy.Spider):
    name = "guba"
    allowed_domains = ["eastmoney.com"]
    start_urls = (
        'http://guba.eastmoney.com/remenba.aspx?type=1',
    )

    def parse(self, response):
        shares_links = response.css('.ngbggulbody .ngbglistdiv')[0:4].css('a')
        for share in shares_links:
        	text = share.xpath('text()')[0].extract()
        	share_href = 'http://guba.eastmoney.com/' + share.xpath('@href')[0].extract()
        	share_id, share_name = text.split(')') # (600000)浦发银行
        	share_id = share_id[1:]
        	yield GubaShare(share_id=share_id, share_name=share_name, share_href=share_href)

class GubaTopicSpider(scrapy.Spider):
	name = "guba_topic"
	allowed_domains = ["eastmoney.com"]

	def __init__(self, id_from=1, id_num=0, *args, **kwargs):
		super(GubaTopicSpider, self).__init__(*args, **kwargs)
		self.id_scope = range(int(id_from), int(id_from)+int(id_num))

	def start_requests(self):
		for each_id in self.id_scope:
			request = scrapy.Request('http://guba.eastmoney.com/news,600000,%u.html' % each_id,
								 callback=self.parse_topic_id)
			request.meta['id'] = each_id
			yield request

	def parse_topic_id(self, response):
		share_name = response.xpath('//span[@id="stockname"]/a/text()')[0].extract()[:-1]
		share_id = response.xpath('//span[@id="stockheadercode"]/a/text()')[0].extract()
		topic_time = response.xpath('//div[@id="zwconbotl"]/text()')[0].extract()[8:]
		# XXX store time into Python builtin time obj "2006-09-18 21:58:35"
		topic_time = time.strptime(topic_time, '%Y-%m-%d %H:%M:%S')
		# Don't use utcfromtimestamp. We just store the local time as UTC time in MongoDB
		# (Though this is wrong, it gives convenience for manipulating per-date operations
		#  in MongoDB)
		topic_time = datetime.fromtimestamp(time.mktime(topic_time))
		topic_author = response.xpath('//div[@id="zwconttbn"]/strong/span/text()')[0].extract()
		topic_title = response.xpath('//div[@id="zwconttbt"]/text()')[0].extract()
		topic_content = ''.join(response.xpath('//div[@id="zwconbody"]/div/node()').extract())
		topic_reply_count = int(re.search('var pinglun_num=(\d+);', response.body).group(1))
		topic_view_count = int(re.search('var num=(\d+);', response.body).group(1))
		yield GubaTopic(topic_id=response.meta['id'],
						topic_time=topic_time,
						topic_author=topic_author,
						topic_title=topic_title,
						topic_content=topic_content,
						topic_reply_count=topic_reply_count,
						topic_view_count=topic_view_count,
						share_id=share_id,
						share_name=share_name,
						)


        
