class WebFileLoader:

    def __init__(self):
        pass

    @staticmethod
    def download(url):
        """
        Copy the contents of a file from a given URL
        to a local file.
        :param url: Url of file to load.
        """
        import urllib2
        webFile = urllib2.urlopen(url)
        localFile = open(url.split('/')[-1], 'w')
        localFile.write(webFile.read())
        webFile.close()
        localFile.close()

#if __name__ == '__main__':
#    import sys
#    if len(sys.argv) == 2:
#        try:
#            WebFileLoader.download(sys.argv[1])
#        except IOError:
#            print 'Filename not found.'
#    else:
#        import os
#        print 'usage: %s http://server.com/path/to/filename' % os.path.basename(sys.argv[0])
