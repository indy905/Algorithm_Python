# 시간 복잡도 : O (n log n)
# worst : O (n^2)
# 공간복잡도 : O(n)


import unittest


def quick_sort(list, start, end):
    if start < end:
        pivot = partition(list, start, end)
        quick_sort(list, start, pivot - 1)
        quick_sort(list, pivot + 1, end)
    return list


def partition(list, start, end):
    pivot = end
    wall = start
    left = start

    while left < pivot:
        if list[left] < list[pivot]:
            list[wall], list[left] = list[left], list[wall]
            wall = wall + 1
        left = left + 1

    list[wall], list[pivot] = list[pivot], list[wall]
    pivot = wall
    return pivot


class unit_test(unittest.TestCase):
    def test(self):
        list = [8, 13, 2, 6, 1, 4]
        self.assertEqual([1,2,4,6,8,13], quick_sort(list, 0, len(list) - 1))

        list = [8, 1, 2, 5, 10, 14, 7, 21]
        self.assertEqual([1, 2, 5, 7, 8, 10, 14, 21], quick_sort(list, 0, len(list) - 1))