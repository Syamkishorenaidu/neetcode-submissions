from collections import defaultdict

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        num_2_hash = {value: i for i, value in enumerate(nums2)}

        for i in nums1:
            result.append(num_2_hash.get(i))
            
        return result


        