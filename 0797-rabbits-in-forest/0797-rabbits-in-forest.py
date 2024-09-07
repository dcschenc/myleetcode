class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # Count the occurrences of each answer
        answer_counter = Counter(answers)      
        # Initialize total number of rabbits reported
        total_rabbits = 0
      
        # Iterate through each unique answer (number_of_other_rabbits) and its count
        for number_of_other_rabbits, count in answer_counter.items():
            # Each rabbit with the same answer (number_of_other_rabbits) forms a group.
            # The size of each group is number_of_other_rabbits + 1 (including itself).
            group_size = number_of_other_rabbits + 1
          
            # Calculate the number of full groups (possibly partial for the last group)
            # by dividing the count of rabbits by the group size and rounding up.
            # This gives the number of groups where each rabbit reports
            # number_of_other_rabbits other rabbits with the same color.
            number_of_groups = math.ceil(count / group_size)
          
            # Add to the total number of rabbits by multiplying the number of groups
            # by the size of the group.
            total_rabbits += number_of_groups * group_size
      
        # Return the total number of rabbits reported
        return total_rabbits
