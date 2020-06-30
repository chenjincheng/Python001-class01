# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from ..items import ScrapyMoviesItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    # 第一次运行，且只运行一次
    def start_requests(self):
        url = 'file:///D:/index.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
            'Cookie' : 'uuid_n_v=v1; uuid=1F401820B95E11EA8E55532676AF0F4AF41FE8F97E5C4729B0B94E46AD3FA877; mojo-uuid=20f3a7cc12fb2a06f2a5000a5ab96acc; _lxsdk_cuid=172fbcd87e3c8-089042fd9b8e51-b791b36-144000-172fbcd87e3c8; _lxsdk=1F401820B95E11EA8E55532676AF0F4AF41FE8F97E5C4729B0B94E46AD3FA877; _csrf=9168db558e10cf4c19acd18727733fd8ffd838d449c56e3fe9b2cc2cb563d49e; mojo-session-id={"id":"2e910fe95029cf2774da33f934d34294","time":1593529453996}; lt=zzMA7xegfdyZO0-6pOQdMDxYUj4AAAAAAAsAADqAh3WgNbfffVfdxuWa7Rem_maGlcdnJhtHjM1Arenzmmfdy07dIWaV2BD7O9cWTw; lt.sig=HKiDA9FlTKDmyYToCupoJXfrsWM; mojo-trace-id=3; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593448430,1593448447,1593526128,1593530487; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593530487; __mta=217488681.1593362450474.1593529454106.1593530487339.28; _lxsdk_s=17305c1ca68-56b-5d2-236%7C%7C5',
        }
        yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        movies = Selector(response).xpath('//*[@class="movie-item film-channel"]')
        for movie in movies :
            item = ScrapyMoviesItem()
            item['movie_name'] = movie.xpath('./div[2]/a/div/div[1]/span[1]/text()').extract_first().strip()
            item['movie_type'] = movie.xpath('./div[2]/a/div/div[2]/text()').extract()[1].strip()
            item['movie_date'] = movie.xpath('./div[2]/a/div/div[4]/text()').extract()[1].strip()
            yield item