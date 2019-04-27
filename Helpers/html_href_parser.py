import urllib.request
from urllib.parse import urljoin
import re


class HtmlHrefParser:
    """
    Class to load html from provided url and parse hrefs (all or with name extension) in it.
    """
    html_data = None

    def __init__(self, url, name_extension=None):
        self.url = url
        self.name_extension = name_extension

    @staticmethod
    def __is_valid_url(url):
        """
        Validates url.
        :param url: Url to validate.
        :return: true if url is valid else false.
        """
        regex = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return url is not None and regex.search(url)

    def fetch(self):
        """
        Loads data from url.
        :return: Body of loaded url.
        """
        if self.__is_valid_url(self.url):
            with urllib.request.urlopen(self.url) as response:
                response_body = str(response.read())
                self.html_data = response_body
                return response_body
        return None

    def parse(self):
        """
        Parse already fetched html or fetch it previously.
        :return: List of href urls.
        """
        re_pattern = r"href=\"([^\"]*)\""
        if self.name_extension:
            re_pattern = r"href=\"([^\"]*." + self.name_extension + ")\""
        if not self.html_data:
            self.fetch()
        relative_urls_list = re.findall(re_pattern, self.html_data)

        # Translate relative url path '../webm_name.webm' to absolute path to resource.
        absolute_urls_set = set(map(lambda u: urljoin(self.url, u), relative_urls_list))

        return list(absolute_urls_set)

