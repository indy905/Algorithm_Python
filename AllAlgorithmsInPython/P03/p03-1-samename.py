# 두 번 이상 나온 이름 찾기
# 입력: 이름이 n개 들어 있는 리스트
# 출력: 이름 n개 중 반복되는 이름의 집합
# 시간복잡도 : O(n^2)

import unittest


def find_same_name(alist):
    n = len(alist)
    result = set()
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if alist[i] == alist[j]:
                result.add(alist[i])
    return result


class unit_test(unittest.TestCase):
    def test(self):
        self.assertEqual({"Tom"}, find_same_name(["Tom", "Jerry", "Bill", "Tom"]))
        self.assertEqual({"Tom", "Bill"}, find_same_name(["Tom", "Jerry", "Bill", "Tom", "Bill"]))
