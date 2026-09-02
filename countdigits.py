class Solution:
    def countDigit(self, n):
        count = 0
        copy = n

        if n == 0:
            return 1

        while copy != 0:
            copy = copy // 10
            count = count + 1

        return count
