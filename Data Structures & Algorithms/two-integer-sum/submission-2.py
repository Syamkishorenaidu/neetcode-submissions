class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        sorted_arr = []

        for i in range(len(nums)):
            sorted_arr.append((nums[i], i))

        sorted_arr.sort()

        i = 0
        j = len(sorted_arr) - 1

        while i < j:

            cur_sum = sorted_arr[i][0] + sorted_arr[j][0]

            if cur_sum < target:
                i += 1

            elif cur_sum > target:
                j -= 1

            else:
                return sorted([sorted_arr[i][1], sorted_arr[j][1]])

        return []