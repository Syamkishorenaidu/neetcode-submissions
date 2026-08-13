class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0
        if len(s) == 1:
            return 0
        else:
            for i, letter in enumerate(s):
                if i != len(s) - 1:
                    result = result + abs(ord(s[i]) - ord(s[i+1]))
        
        return result

                

        