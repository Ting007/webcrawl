import scrapy
import csv
import sys

class QuotesSpider(scrapy.Spider):
    name = "git"
    start_urls = []
    csvfile = open("JavaURL.csv", "r")
    reader = csv.reader(csvfile)
    for row in reader:
    	start_urls.extend(row)
    	

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'git-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        quote = response.css("tr.js-navigation-item")
        for icon in quote.css("td.content"):
            file = icon.css("a.js-navigation-open::text").extract_first()
            # yield{
            #     'file':icon.css("a.js-navigation-open::text").extract_first()
            # }
            if file == "build.xml":
                with open('antFile.csv', 'a') as output:
                	output.write(str(response.url))
                	output.write('\n')

                    