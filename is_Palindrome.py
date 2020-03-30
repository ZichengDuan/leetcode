class Solution:
    def isPalindrome(self, x: int) -> bool:
            """
            test whether a number is palindrom
            :param x:
            :return: Bool
            """
            return False if x < 0 else str(x)[::-1] == str(x)
            # if x < 0:
            #     return False
            # else:
            #     y = str(x)[::-1]
            #     return y == str(x)