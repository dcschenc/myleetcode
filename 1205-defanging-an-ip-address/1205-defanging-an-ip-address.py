class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ''
        for s in address.split('.'):
            res += s + '[.]'
        return res[:-3]
        