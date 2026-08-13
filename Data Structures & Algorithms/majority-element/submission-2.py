class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current_high = 0
        majority = 0

        for i in nums:
            if current_high == i:
                majority += 1
            elif majority == 0:
                current_high = i
                majority += 1
            else:
                majority -= 1
        
        return current_high