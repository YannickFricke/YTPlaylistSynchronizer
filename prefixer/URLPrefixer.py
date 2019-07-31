class URLPrefixer:
    def __init__(self, prefix: str):
        self.prefix = prefix

    def prefixUrl(self, url):
        return self.prefix + url
