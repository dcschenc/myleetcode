class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_level = []        
        for i in range(rowIndex+1):
            curr_level = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    curr_level.append(1)
                else:
                    curr_level.append(prev_level[j-1] + prev_level[j])
            # print(curr_level)
            prev_level = curr_level
        return curr_level

        ### recursive ####
        if rowIndex == 0:
            return [1]      
        else:
            prev_row = self.getRow(rowIndex-1)
            res = []
            for j, val in enumerate(prev_row):
                if j == 0:
                    res.append(1)
                else:
                    res.append(prev_row[j-1] + prev_row[j])
            res.append(1)
            return res
            
            