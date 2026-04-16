class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        n, m = len(num1), len(num2)
        res = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                
                pos1 = i + j
                pos2 = i + j + 1

                total = mul + res[pos2]

                res[pos2] = total % 10
                res[pos1] += total // 10

        # convert to string
        result = ''.join(map(str, res)).lstrip('0')
        return result