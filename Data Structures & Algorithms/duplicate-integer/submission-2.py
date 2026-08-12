from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) == 0:
            return False

        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1
        return True if max(freq.values()) > 1 else False
        