class Solution:
    def calculate(self, s: str) -> int:
        plus_ele = [self.sub_calculate(x.strip()) for x in s.split('+')]
        return int(sum(plus_ele))

    def sub_calculate(self, s: str):
        if '-' in s:
            minus_ele = [x.strip() for x in s.split('-')]
            res = self.sub_calculate(minus_ele[0])
            for i in range(1, len(minus_ele)):
                res = res - self.sub_calculate(minus_ele[i])
            return res

        elif '*' in s or '/' in s:
            s = s.strip()
            i = len(s) - 1
            while i >= 0 and s[i] != '/' and s[i] != '*':
                i -= 1
            if s[i] == '*':
                return self.sub_calculate(s[:i].strip()) * self.sub_calculate(s[i + 1:].strip())
            elif s[i] == '/':
                return int(self.sub_calculate(s[:i].strip()) / self.sub_calculate(s[i + 1:].strip()))

        elif s.isdigit():
            return int(s.strip())