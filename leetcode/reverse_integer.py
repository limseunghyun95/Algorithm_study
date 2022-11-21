# source: https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        flag = -1 if x < 0 else 1

        answer = flag * int(str(abs(x))[::-1])
        if answer not in range(-1 * (2**31), (2**31) + 1):
            return 0
        else:
            return answer