# 연속한 숫자의 곱을 구하는 알고리즘
# 입력: n
# 출력: 1부터 n까지 연속한 숫자를 곱한 값

import unittest

# 시간복잡도 : O(n)
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


class unit_test_factorial(unittest.TestCase):
    def test(self):
        self.assertEqual(1, factorial(1))
        self.assertEqual(120, factorial(5))
        self.assertEqual(3628800, factorial(10))

# 시간복잡도 : O(n)
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


class unit_test_factorial_recursive(unittest.TestCase):
    def test(self):
        self.assertEqual(1, factorial_recursive(1))
        self.assertEqual(120, factorial_recursive(5))
        self.assertEqual(3628800, factorial_recursive(10))