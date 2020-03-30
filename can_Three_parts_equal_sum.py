class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False
        tmp_sum = 0
        for i in range(len(A)):
            tmp_sum += A[i]
            if tmp_sum == s / 3:
                break
        if i >= len(A) - 1:
            return False

        for j in range(i + 1, len(A)):
            tmp_sum += A[j]
            if tmp_sum == 2 * s / 3:
                if j >= len(A) - 1:
                    return False
                return True
            else:
                continue
        return False