class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2251.Number%20of%20Flowers%20in%20Full%20Bloom
        start, end = sorted(a for a, _ in flowers), sorted(b for _, b in flowers)
        return [bisect_right(start, p) - bisect_left(end, p) for p in people]

        persons = people
        # Extract all unique times (start, end + 1, and query times)
        times = set()
        for start, end in flowers:
            times.add(start)
            times.add(end + 1)
        for person in persons:
            times.add(person)
        
        # Sort the unique times
        sorted_times = sorted(times)
        
        # Coordinate compression: map each unique time to a smaller range
        time_to_index = {time: index for index, time in enumerate(sorted_times)}
        
        # Initialize the difference array with the size of unique times
        diff = [0] * (len(sorted_times) + 1)
        
        # Populate the difference array using compressed indices
        for start, end in flowers:
            diff[time_to_index[start]] += 1
            diff[time_to_index[end + 1]] -= 1
        
        # Compute the prefix sums on the compressed difference array
        bloom_counts = [0] * len(sorted_times)
        current_bloom = 0
        for i in range(len(sorted_times)):
            current_bloom += diff[i]
            bloom_counts[i] = current_bloom
        
        # Answer the queries using the compressed indices
        result = []
        for person in persons:
            index = time_to_index[person]
            result.append(bloom_counts[index])
        
        return result
