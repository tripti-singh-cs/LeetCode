class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        # skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # sign check
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        num = 0

        # read digits
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num = num * sign

        # clamp to 32-bit range
        if num < -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1

        return num       