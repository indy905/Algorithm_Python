import unittest

#  0과 1부터 시작해서 바로 앞의 두 수를 더한 값을 다음 값으로 추가하는 방식으로 만든 수열을 피보나치 수열이라고 합니다.
# 즉, 0+1=1, 1+1=2, 1+2=3이므로 피보나치 수열은 다음과 같습니다.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 …

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)



class unit_test_fibonacci(unittest.TestCase):
    def test(self):
        self.assertEqual(13, fibonacci(7))
