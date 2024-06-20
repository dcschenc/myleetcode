class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dict = defaultdict(set)
        for w in dictionary:
            abbr = w
            if len(w) > 2:
                abbr = w[0] + str(len(w[1:-1])) + w[-1]           
                
            self.dict[abbr].add(w)
        

    def isUnique(self, word: str) -> bool:
        abbr = word
        if len(word) > 2:
            abbr = word[0] + str(len(word[1:-1])) + word[-1]    
        if abbr not in self.dict or abbr in self.dict and len(self.dict[abbr]) == 1 and word in self.dict[abbr]:
            return True
        return False
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)