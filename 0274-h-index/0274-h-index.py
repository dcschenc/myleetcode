class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # [0, 1, 3, 5, 6]
        citations.sort()  # Sort the citations in non-decreasing order
        n = len(citations)
        
        h_index = 0
        for i in range(n):
            # Calculate the h-index for the current citation count
            h_index = max(h_index, min(citations[i], n - i))
        
        return h_index

        citations.sort(reverse=True)
        n = len(citations)
        # print(citations)

        for i in range(n):
            if i >= citations[i]:
                return i
        return i+1

        if not intervals:
            return []

        

        
