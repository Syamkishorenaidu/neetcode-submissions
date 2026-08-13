class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        seq_count, max_seq_count = 0, 0

        for i in range(len(s)):
            if s[i] != " ":
                seq_count +=1
            else:
                max_seq_count =  seq_count if seq_count !=0 else max_seq_count
                seq_count = 0
            
        return max_seq_count if seq_count == 0 else seq_count



        