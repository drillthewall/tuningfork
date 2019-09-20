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

		# <ul class="artist-list review__title-artist"><li>Lightning Bolt</li></ul>

		# albumName = response.xpath("//h1[@class='single-album-tombstone__review-title']/text()").extract_first()
		# # yield {'AlbumName': albumName}

		# artist = response.xpath('//ul[@class="artist-links artist-list single-album-tombstone__artist-links"]/li/a/text()').extract_first()		
		# # yield {'Artist': artist}

		# # reviewer = response.xpath('//ul[@class="authors"]/li/a/@href').extract()
		# # yield {'Reviewer': reviewer}

		# score = response.xpath("//span[@class='score']/text()").extract_first()
		# # yield {'Score': score}

		# text = response.xpath("//div[@class='contents dropcap']/p/text()").extract()
		# # yield {'ReviewText': text}

		# item['albumName'] = albumName
		# item['artist'] =  artist
		# item['score'] = score
		# item['text'] = text

		# yield item

		# for paragraph in response.xpath("//div[@class='contents dropcap']/p"):
		# 	yield {
		# 		'review_text': paragraph.xpath(".//text()").extract()
		# 	} 

# //*[@id="review-article-5929d9555e6ef959693247bd"]/div[3]/div[1]/ul[1]/li/a/text()