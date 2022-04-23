class Codec:
    short_URL_DB, URL_DB = {}, {}
    chars = string.ascii_letters + string.digits
    
    def create_URL(self):
        code = ''.join(random.choice(self.chars) for i in range(6))
        return "http://tinyurl.com/" + code
    
    def encode(self, longURL: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longURL in self.URL_DB:
            return self.URL_DB[longURL]
        
        shortURL = self.create_URL()
        
        while shortURL in self.short_URL_DB:
            shortURL = create_URL()
            
        self.short_URL_DB[shortURL] = longURL
        self.URL_DB[longURL] = shortURL
        
        return shortURL

    def decode(self, shortURL: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short_URL_DB[shortURL]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))