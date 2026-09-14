class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create the dictionary for storing
        freq = dict()

        # Pass over the elements
        for num in nums:
            # Check if the number exists in the dictionary
            if num not in freq:
                freq[num] = 1
                continue
            freq[num] += 1
        return sorted(freq, key=freq.get, reverse=True)[:k]