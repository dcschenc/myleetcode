class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        barcode_count = Counter(barcodes)
        max_heap = [(-freq, barcode) for barcode, freq in barcode_count.items()]
        heapq.heapify(max_heap)
        
        result = [0] * len(barcodes)
        index = 0        
        while max_heap:
            freq, barcode = heapq.heappop(max_heap)            
            while freq < 0:
                result[index] = barcode
                index += 2
                freq += 1                
                if index >= len(barcodes):
                    index = 1        
        return result
