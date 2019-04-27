class WebFileLoader:

    def __init__(self):
        pass

    @staticmethod
    def __reporthook(count, block_size, total_size):
        import time
        import sys
        global start_time
        if count == 0:
            start_time = time.time()
            return
        duration = time.time() - start_time
        if duration <= 0:
            return
        progress_size = int(count * block_size)
        speed = int(progress_size / (1024 * duration))
        percent = int(count * block_size * 100 / total_size)
        sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                         (percent, progress_size / (1024 * 1024), speed, duration))
        sys.stdout.flush()

    @staticmethod
    def save(url, folder_name=''):
        import urllib.request
        path = url.split('/')[-1]
        if len(folder_name) > 0:
            path = folder_name + '/' + path
        urllib.request.urlretrieve(url, path, WebFileLoader.__reporthook)
