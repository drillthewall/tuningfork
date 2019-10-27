import scrapy

URL = 'https://pitchfork.com/best/high-scoring-albums/?page=%d'

class linkScraper (scrapy.Spider):
	name = "linkScraper"
	
	start_urls = [URL % 1]

	def __init__(self):
		self.page_number = 1

	def parse(self, response):

		if self.page_number >= 386:
			raise CloseSpider('no more pages')

		for review in response.xpath('//div[@class="review"]'):
			yield {
				'url' : review.xpath('.//a/@href').extract_first(),
				'artist' : review.xpath('.//ul/li/text()').extract_first(),
				'album' : review.xpath('.//h2/text()').extract_first()
			}

		self.page_number += 1
		newurl = URL % self.page_number
		yield scrapy.Request(url=newurl, callback=self.parse)