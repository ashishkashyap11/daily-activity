class Solution:
    def fpowr(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        a = self.fpowr(x, n // 2)
        if n % 2 != 0:
            return a * a * x
        else:
            return a * a

    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.fpowr(x, n)
        else:
            return 1 / self.fpowr(x, -n)
