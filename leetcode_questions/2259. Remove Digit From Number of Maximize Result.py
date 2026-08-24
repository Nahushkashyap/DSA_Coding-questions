# Question :- https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_value = 0
        for i in range(len(number)):
            if number[i] == digit:
                number_excluding_digit = int(number[:i] + number[i + 1 :])
                if max_value < number_excluding_digit:
                    max_value = number_excluding_digit
        return str(max_value)
