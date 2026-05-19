class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        n = len(num)
        for i in range(1, n):

            for j in range(i + 1, n):

                first = num[:i]
                second = num[i:j]

                if (len(first) > 1 and first[0] == '0') or \
                   (len(second) > 1 and second[0] == '0'):
                    continue

                if self.check_sequence(first, second, num[j:]):
                    return True

        return False


    def check_sequence(self, first, second, remaining):

        if remaining == "":
            return True

        total = str(int(first) + int(second))

        if not remaining.startswith(total):
            return False

        return self.check_sequence(
            second,
            total,
            remaining[len(total):]
        )