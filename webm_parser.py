import urllib2
import urlparse
import sys
import re

def fetch_url(url):
    response = urllib2.urlopen(url)
    response_body = response.read()
    return response_body

def pars_html_for_webm_urls_list(html_string):
    re_pattern = r"href=\"([^\"]*.webm)\""
    relative_urls_list = re.findall(re_pattern, html_string)
    absolute_urls_list = []
    # Translate relative url path '../webm_name.webm' to absolute path to resource.
    for relative_webm_url in relative_urls_list:
        absolute_webm_url = urlparse.urljoin(url, relative_webm_url)
        absolute_urls_list.append(absolute_webm_url)
    return absolute_urls_list

def is_valid_url(url):
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)


url = sys.argv[1]
if (is_valid_url(url)):
    html_string = fetch_url(url)
    webm_urls_list = pars_html_for_webm_urls_list(html_string)

    # Make set from webm list to remove repeats.
    webm_urls_set = set(webm_urls_list)
    print( '\n'.join(webm_urls_set) )
else:
    print("url: " +  url + "is invalid.") 
