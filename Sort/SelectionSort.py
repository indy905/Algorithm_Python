#시간복잡도 : O(n^2)
#공간복잡도 : O(n)

import unittest

def selection_sort(list):
    for i in range(len(list) - 1):
        idx_min = i
        j = i + 1
        while j < len(list):
            if list[j] < list[idx_min]:
                idx_min = j
            j = j + 1

        if idx_min is not i:
            list[idx_min], list[i] = list[i], list[idx_min]
    return list

class unit_test(unittest.TestCase):
    def test(self):
        self.assertEqual([1,2,3,4,5,6], selection_sort([4,3,5,2,6,1]))
        self.assertEqual([1,2,3,4,5,6], selection_sort([6,5,4,3,2,1]))
        self.assertEqual([1,2,3,4,5,6], selection_sort([1,6,2,5,3,4]))