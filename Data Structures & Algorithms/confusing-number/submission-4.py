class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalid_numbers = [2, 3, 4, 5, 7]
        valid_numbers = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

        reversed_number = ''

        for x in str(n):
            if int(x) in invalid_numbers:
                return False
            else:
                # Add to the FRONT so the number is reversed
                reversed_number = str(valid_numbers.get(int(x))) + reversed_number

        # Convert string to integer before comparison
        return False if int(reversed_number) == n else True