class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        v = length * width * height
        bulky = int(any(x >= 10000 for x in (length, width, height)) or v >= 10**9)
        heavy = int(mass >= 100)
        i = heavy << 1 | bulky
        d = ['Neither', 'Bulky', 'Heavy', 'Both']
        return d[i]

        
        bulky = False
        if length >= 10 ** 4 or width >= 10 ** 4 or height >= 10 ** 4 or mass >= 10 ** 4:
            bulky = True
        if length * width * height >= 10 ** 9:
            bulky = True
        heavy = False
        if mass >= 100: 
            heavy = True

        if bulky and heavy:
            return 'Both'
        elif not bulky and not heavy:
            return 'Neither'
        elif bulky and not heavy:
            return 'Bulky'
        elif heavy and not bulky:
            return 'Heavy'
