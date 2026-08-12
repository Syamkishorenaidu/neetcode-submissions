
class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        res = []
        for i in range(len(arr)):
            if i == len(arr) - 1:
                res.append(-1)
            else: 
                res.append(max(arr[i+1:]))
        return res
        