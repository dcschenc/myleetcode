class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ''
        for s in strs:
            encoded = encoded + str(len(s)) + '/' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded = []
        while len(s) > 0:
            idx = s.find('/')
            length = int(s[:idx])
            w = s[idx+1: idx + 1 + length]
            decoded.append(w)
            s = s[idx + 1 + length:]
        return decoded
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))