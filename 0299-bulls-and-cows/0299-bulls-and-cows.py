class Solution:
    def getHint(self, secret: str, guess: str) -> str:        
        countA, countB = 0, 0
        hmS, hmG = {}, {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                countA += 1
            else:
                hmS[secret[i]] = 1 + hmS.get(secret[i],0)
                hmG[guess[i]] = 1 + hmG.get(guess[i], 0)
        for k, v in hmG.items():
            if k in hmS:
                countB += min(hmG[k], hmS[k])
        return str(countA) + 'A' + str(countB) + 'B'