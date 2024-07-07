class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1109.Corporate%20Flight%20Bookings

        answer = [0] * n
        # Process each booking
        for booking in bookings:
            first, last, seats = booking
            answer[first - 1] += seats  # Increment seats for the first flight
            if last < n:  # If last flight is not the last in the list, decrement seats for the next flight
                answer[last] -= seats
        
        # Compute the cumulative sum using prefix sum
        for i in range(1, n):
            answer[i] += answer[i - 1]
        
        return answer