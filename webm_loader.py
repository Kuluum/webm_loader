import os
import sys
from time import gmtime, strftime
from Helpers.html_href_parser import HtmlHrefParser
from Helpers.web_file_loader import WebFileLoader
url = sys.argv[1]

hrefParser = HtmlHrefParser(url, 'webm')

hrefParser.fetch()
url_list = hrefParser.parse()

now_str = strftime("downloads/%Y-%m-%d_%H-%M-%S", gmtime())
if not os.path.exists(now_str):
    os.makedirs(now_str)

for url in url_list:
    print("Loading " + url + " ...")
    WebFileLoader.save(url, now_str)
    print("\n")
print('Succeeded')
