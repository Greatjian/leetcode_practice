# 535. Encode and Decode TinyURL

TinyURL is a URL shortening service where you enter a URL such as 

    https://leetcode.com/problems/design-tinyurl 
    
and it returns a short URL such as 

    http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

## Method:

    class Codec:
    
        def __init__(self):
            self.d={}
            
        def encode(self, longUrl):
            """Encodes a URL to a shortened URL.
            
            :type longUrl: str
            :rtype: str
            """
            h=hash(longUrl)
            self.d[h]=longUrl
            return h
    
        def decode(self, shortUrl):
            """Decodes a shortened URL to its original URL.
            
            :type shortUrl: str
            :rtype: str
            """
            return self.d[shortUrl]
    
    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.decode(codec.encode(url))
    
hash to random:

    class Codec:
        def __init__(self):
            self.code2url = {}
    
        def encode(self, longUrl):
            """Encodes a URL to a shortened URL.
            
            :type longUrl: str
            :rtype: str
            """
            code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
            self.code2url[code] = longUrl
            return 'http://tinyurl.com/' + code
                    
                
    
        def decode(self, shortUrl):
            """Decodes a shortened URL to its original URL.
            
            :type shortUrl: str
            :rtype: str
            """
            code = shortUrl.split('/')[-1]
            return self.code2url[code]
    
    
    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.decode(codec.encode(url))