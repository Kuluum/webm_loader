import sys
from html_href_parser import HtmlHrefParser
from web_file_loader import WebFileLoader
url = sys.argv[1]

hrefParser = HtmlHrefParser(url, 'webm')

hrefParser.fetch()
url_list = hrefParser.parse()

for url in url_list:
    print "Loading " + url + " ..."
    WebFileLoader.save(url)
    print "\n"
