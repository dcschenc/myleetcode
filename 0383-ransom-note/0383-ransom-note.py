from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_dict = Counter(magazine)
        r_dict = Counter(ransomNote)
        for k, v in r_dict.items():
            if k not in m_dict:
                return False
            if v > m_dict[k]:
                return False
        return True