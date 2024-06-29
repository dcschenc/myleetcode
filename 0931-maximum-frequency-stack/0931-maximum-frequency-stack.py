class FreqStack:

    def __init__(self):
        # Initialize a dictionary to count the frequency of elements
        self.freq_counter = defaultdict(int)
        # A dictionary that maps frequencies to a list of elements with that frequency
        self.freq_dict = defaultdict(list)
        # Variable to keep track of the maximum frequency observed so far
        self.max_freq = 0

    def push(self, val: int) -> None:
        """
        Pushes an integer onto the stack and updates the structures tracking element frequency.
        """
        # Increment the frequency count for the given value
        self.freq_counter[val] += 1
        # Add the value to the list of values that have the new frequency count
        self.freq_dict[self.freq_counter[val]].append(val)
        # Update the maximum frequency if it's exceeded by this value's frequency
        self.max_freq = max(self.max_freq, self.freq_counter[val])

    def pop(self) -> int:
        """
        Pops and returns the most frequent integer from the stack. If there is a tie,
        it returns the integer closest to the top of the stack.
        """
        # Pop the value from the list corresponding to the maximum frequency
        val = self.freq_dict[self.max_freq].pop()
        # Decrement the frequency count for that value
        self.freq_counter[val] -= 1
        # If there are no more elements with the current maximum frequency, decrease the maximum frequency
        if not self.freq_dict[self.max_freq]:
            self.max_freq -= 1
        # Return the value
        return val

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()