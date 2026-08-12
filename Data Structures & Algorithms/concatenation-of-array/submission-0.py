class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        results = []
        for i in range(2):
            for j in nums:
                results.append(j)
        return results

        