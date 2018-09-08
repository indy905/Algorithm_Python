# 시간복잡도 : O(n^2)

import unittest


def insertion_sort(list):
    for idx, valueToInsert in enumerate(list):
        holdPosition = idx

        while holdPosition > 0 and list[holdPosition - 1] > valueToInsert:
            list[holdPosition - 1], list[holdPosition] = list[holdPosition], list[holdPosition - 1]
            holdPosition = holdPosition - 1

    return list


def insertion_sort2(list):
    for i in range(1, len(list)):
        j = i - 1
        key = list[i]
        while list[j] > key and j >= 0:
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = key
    return list


class unit_test(unittest.TestCase):
    def test(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], insertion_sort2([4, 6, 1, 3, 5, 2]))
        self.assertEqual([1, 2, 3, 4, 5, 6], insertion_sort2([6, 4, 3, 1, 2, 5]))
        self.assertEqual([1, 2, 3, 4, 5, 6], insertion_sort2([6, 5, 4, 3, 2, 1]))