import scrapy
from ..items import PitchforkScraperItem
from pathlib import Path
import json
from html_text import extract_text
# import BNMlinks.json

class PitchforkSpider (scrapy.Spider):
	name = "pitchfork_spider"
	# start_urls = ['https://pitchfork.com/reviews/albums/the-carters-everything-is-love/']

	def start_requests(self):
		url = 'https://pitchfork.com'
		###!!!!!!!! CHANGE DIRECTORY !!!!!!!!###
		path = Path('C:\\Users\\drillthewall\\Desktop\\tuningfork\\pitchfork_scraper\\pitchfork_scraper\\spiders\\eightPlusLinks.json')
		with path.open() as json_file:
			data = json.load(json_file)
			for review in data:
				appendurl = review['url']
				s = url + appendurl
				# print('------S IS',s)
				yield scrapy.Request(s,self.parse)


	def parse(self, response):

		item = PitchforkScraperItem()

		album = response.xpath("//h1[@class='single-album-tombstone__review-title']/text()").get()
		# yield {'AlbumName': albumName}

		artist = response.xpath('//ul[@class="artist-links artist-list single-album-tombstone__artist-links"]/li/a/text()').getall()		
		# yield {'Artist': artist}

		year = response.xpath('//span[@class="single-album-tombstone__meta-year"]').get()
		year = extract_text(year)
		year = year[2:]

		genre = response.xpath('//a[@class="genre-list__link"]/text()').getall()

		reviewer = response.xpath('//a[@class="authors-detail__display-name"]/text()').get()
		# yield {'Reviewer': reviewer}

		score = response.xpath("//span[@class='score']/text()").get()
		# yield {'Score': score}

		text = ""
		for paragraph in response.xpath("//div[@class='contents dropcap']/p"):
			html = paragraph.get()
			text = text + " " + extract_text(html)

		italic = response.xpath("//em/text()").getall()

		links = response.xpath("//div[@class='contents dropcap']//a/text()").getall()

		# for link in response.xpath("//div[@class='contents dropcap']//a[contains(@href,'reviews')]"):
		# 	yield {
		# 		'artistLinks': link.get()
		# 	}

		albumLinks = response.xpath("//div[@class='contents dropcap']//a[contains(@href,'reviews')]//text()").getall()

		artistLinks = response.xpath("//div[@class='contents dropcap']//a[contains(@href,'artists')]//text()").getall()

		# html = response.xpath("//div[@class='contents dropcap']").get()
		# text = extract_text(html)
		# text = initext.xpath('normalize_space()').extract()
		# yield {'ReviewText': text}
		# item['artistLinks'] = artistLinks
		
		item['album'] = album
		item['artist'] =  artist
		item['year'] = year
		item['score'] = score
		item['genre'] = genre
		item['reviewer'] = reviewer
		item['text'] = text
		item['italic'] = italic
		item['links'] = links
		item['albumLinks'] = albumLinks
		item['artistLinks'] = artistLinks

		yield item

		# for paragraph in response.xpath("//div[@class='contents dropcap']/p").:
		# 	yield {
		# 		'review_text': paragraph.xpath(".//text()").extract()
		# 	} 

# //*[@id="review-article-5929d9555e6ef959693247bd"]/div[3]/div[1]/ul[1]/li/a/text()