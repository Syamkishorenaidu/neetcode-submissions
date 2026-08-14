class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        left_point = 0
        right_point = len(nums) - 1

        while left_point <= right_point:
            if nums[right_point] == val:
                nums[right_point] = "_"
                right_point -= 1
            elif nums[left_point] == val:
                nums[left_point] = nums[right_point]
                nums[right_point] = "_"
                left_point += 1
                right_point -= 1
            else: 
                left_point += 1


        return right_point + 1
                