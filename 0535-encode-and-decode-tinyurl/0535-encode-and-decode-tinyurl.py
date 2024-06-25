import uuid
class Codec:
    # https://github.com/doocs/leetcode/tree/main/solution/0500-0599/0535.Encode%20and%20Decode%20TinyURL
    def __init__(self):
        self.hm = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        code = uuid.uuid4()
        self.hm[f'http//tinyurl/{code}'] =  longUrl
        return f'http//tinyurl/{code}'

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hm[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))