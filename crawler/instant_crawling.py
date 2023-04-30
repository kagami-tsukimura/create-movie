from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(storage={'root_dir': './Penguin'})
google_crawler.crawl(keyword='Penguin', max_num=10)
