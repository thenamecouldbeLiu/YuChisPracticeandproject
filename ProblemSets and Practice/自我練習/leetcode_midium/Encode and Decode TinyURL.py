# -*- coding: utf-8 -*-
"""
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

"""
import random
class Codec(object):
    def __init__(self):
        self.Url_dict= {}
        
    def encode(self,longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        tiny_head = "http://tinyurl.com/"
        random_list = [chr(i) for i in range(97,123)]+[chr(i) for i in range(65,91)]+[i for i in range(10)]
        end = random.choices(random_list,k=6)
        tiny_end = ""
        for i in end:
            tiny_end+=str(i)
        tiny_Url = tiny_head+tiny_end
        
        self.Url_dict[tiny_Url] = longUrl
        return tiny_Url
    
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        try:
            return self.Url_dict[shortUrl]
        except:
            print("No such tiny url")

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))