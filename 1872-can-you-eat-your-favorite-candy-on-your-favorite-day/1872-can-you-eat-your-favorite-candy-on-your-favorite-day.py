class Solution:
    def canEat(self, candies_count: List[int], queries: List[List[int]]) -> List[bool]:
        # Use accumulate function with initial=0 to create a prefix sum array
        # where s[i] represents the total number of candies up to (but not including) index i
        prefix_sum = list(accumulate(candies_count, initial=0))
      
        # Initialize an empty list to store the answer to each query
        answer_list = []
      
        # Iterate through each query in the queries list
        for candy_type, day, max_candies_per_day in queries:
            # Calculate the least number of candies the user could eat
            least_candies_eaten = day
            # Calculate the most number of candies the user could eat
            most_candies_eaten = (day + 1) * max_candies_per_day
          
            # Determine if the user can eat at least one candy of type 'candy_type'
            # by checking if they would still have candies left on the 'day'
            # and also making sure they won't run out of candies before the day
            can_eat = least_candies_eaten < prefix_sum[candy_type + 1] and most_candies_eaten > prefix_sum[candy_type]
          
            # Add the result to the answer list
            answer_list.append(can_eat)
      
        # Return the list of answers for each query
        return answer_list
