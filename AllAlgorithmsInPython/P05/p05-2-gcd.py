import unittest

# 최대공약수 구하기
# 입력: a, b
# 출력: a와 b의 최대공약수

def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


class unit_test_gcd_recursive(unittest.TestCase):
    def test(self):
        self.assertEqual(1, gcd_recursive(1, 5))
        self.assertEqual(3, gcd_recursive(3, 6))
        self.assertEqual(12, gcd_recursive(60, 24))
        self.assertEqual(27, gcd_recursive(81, 27))

