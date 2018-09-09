import unittest
# 문제 1의 1부터 n까지의 합 구하기를 재귀 호출로 만들어 보세요.

# 시간복잡도 : O(n)
def sum_recursive(n):
    if n <= 1:
        return 1
    return n + sum_recursive(n - 1)


class unit_test_sum_recursive(unittest.TestCase):
    def test(self):
        self.assertEqual(55, sum_recursive(10))
        self.assertEqual(5050, sum_recursive(100))


# 문제 2의 숫자 n개 중에서 최댓값 찾기를 재귀 호출로 만들어 보세요.
def find_max_recursive(alist):
    if len(alist) <= 1:
        return alist[0]
    max_n_1 = find_max_recursive(alist[:len(alist)-1])
    if max_n_1 > alist[len(alist)-1]:
        return max_n_1
    else:
        return alist[len(alist)-1]


class unit_test_find_max_recursive(unittest.TestCase):
    def test(self):
        self.assertEqual(92, find_max_recursive([17, 92, 18, 33, 58, 7, 33, 42]))
        self.assertEqual(100, find_max_recursive([17, 92, 18, 33, 58, 7, 33, 100, 42]))
