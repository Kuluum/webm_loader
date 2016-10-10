class WebFileLoader:

    def __init__(self):
        pass

   # @staticmethod
   # def download(url):
   #     """
   #     Copy the contents of a file from a given URL
   #     to a local file.
   #     """
   #     import urllib2
   #     webFile = urllib2.urlopen(url)
   #     localFile = open(url.split('/')[-1], 'w')
    #    localFile.write(webFile.read())
    #    webFile.close()
    #    localFile.close()

    @staticmethod
    def __reporthook(count, block_size, total_size):
        import time
        import sys
        global start_time
        if count == 0:
            start_time = time.time()
            return
        duration = time.time() - start_time
        progress_size = int(count * block_size)
        speed = int(progress_size / (1024 * duration))
        percent = int(count * block_size * 100 / total_size)
        sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                         (percent, progress_size / (1024 * 1024), speed, duration))
        sys.stdout.flush()

    @staticmethod
    def save(url):
        import urllib
        urllib.urlretrieve(url, url.split('/')[-1], WebFileLoader.__reporthook)