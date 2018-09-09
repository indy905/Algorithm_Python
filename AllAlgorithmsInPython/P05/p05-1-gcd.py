# 최대공약수 구하기
# 입력: a, b
# 출력: a와 b의 최대공약수


import unittest

# 시간복잡도 : O(n)
def find_gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1


class unit_test_find_gcd(unittest.TestCase):
    def test(self):
        self.assertEqual(1, find_gcd(1, 5))
        self.assertEqual(3, find_gcd(3, 6))
        self.assertEqual(12, find_gcd(60, 24))
        self.assertEqual(27, find_gcd(81, 27))

