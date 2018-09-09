# n명 중 두 명을 뽑아 짝을 짓는다고 할 때 짝을 지을 수 있는 모든 조합을 출력하는 알고리즘을 만들어 보세요.
# 예를 들어 입력이 리스트 ["Tom", "Jerry", "Mike"]라면 다음과 같은 세 가지 경우를 출력합니다.'
# Tom - Jerry
# Tom - Mike
# Jerry - Mike
# 시간복잡도 : O(n^2)
import unittest


def make_pair(alist):
    lenth = len(alist)
    result = set()
    for i in range(0, lenth - 1):
        for j in range(i + 1, lenth):
            result.add(alist[i] + "-" + alist[j])
    return result


class unit_test(unittest.TestCase):
    def test(self):
        self.assertEqual({"Tom-Jerry", "Tom-Mike", "Jerry-Mike"}, make_pair(["Tom", "Jerry", "Mike"]))


# 다음 식을 각각 대문자 O 표기법으로 표현해 보세요.
# A 65536 -> O(1)
# B n-1 -> O(n)
# C 2n^2/3 + 10000n O(n^2)
# D 3n^4 + 4n^3 + 5n^2 + 6n + 7 -> O(n^4)