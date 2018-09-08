# 시간복잡도 : O(n^2)
# 공간복잡도 : O(1)

import unittest

def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


class unit_test(unittest.TestCase):
    def test(self):
        self.assertEqual([1,2,3,4,5,6], bubble_sort([2,4,5,6,1,3]))
        self.assertEqual([1,2,3,4,5,6], bubble_sort([6,5,4,3,2,1]))
        self.assertEqual([1,2,3,4,5,6], bubble_sort([6,1,5,2,4,3]))