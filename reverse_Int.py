class Solution:
    def reverse(self, x: int) -> int:
        flag = True
        if x < 0:
            flag = False

        tmp = int(str(abs(x))[::-1])
        if not flag:
            tmp = 0 - tmp
        if tmp > 2147483647 or tmp < -2147483648:
            return 0
        else:
            return tmp