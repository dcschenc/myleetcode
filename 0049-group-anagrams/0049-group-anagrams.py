class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in hm:
                hm[key].append(s)
            else:
                hm[key] = [s]
        return hm.values()

        ## time complexity: O(nklogk)
        