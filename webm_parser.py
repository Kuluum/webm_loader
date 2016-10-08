import sys
from html_href_parser import HtmlHrefParser

url = sys.argv[1]

hrefParser = HtmlHrefParser(url, 'webm')

hrefParser.fetch()
print '\n'.join(hrefParser.parse())

#if is_valid_url(url):
#    html_string = fetch_url(url)
#    webm_urls_list = parse_html_for_webm_urls_list(html_string)

    # Make set from webm list to remove repeats.
#    webm_urls_set = set(webm_urls_list)
#    print('\n'.join(webm_urls_set))
#else:
#    print("url: " + url + "is invalid.")
