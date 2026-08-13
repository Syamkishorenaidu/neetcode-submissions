class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        current_index = 0
        total_distance = 0
        for j in word:
            for i in range(len(keyboard)):
                if j == keyboard[i]:
                    total_distance += abs(current_index - i)
                    current_index = i
        return total_distance




        