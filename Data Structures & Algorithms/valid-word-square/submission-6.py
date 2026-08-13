class Solution:
    def validWordSquare(self, words: List[str]) -> bool:

        for i in range(len(words)):
            for j in range(len(words[i])):

                # Check if the j-th row exists
                if j >= len(words):
                    return False

                # Check if the i-th character exists
                # in the j-th row
                if i >= len(words[j]):
                    return False

                # Compare row character with column character
                if words[i][j] != words[j][i]:
                    return False

        return True