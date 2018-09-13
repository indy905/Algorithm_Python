# worst cast : O(n log n)
# best case : O(n log n)
# get max, min value : O(1)
# heapsort is an in-place algorithm

# max heap tree : root가 가장 큰 값이고 parent가 childs보다 큰 값일 때

# heapify : 일반적인 tree를 heap tree로 변경
def heapify(list, size):
    p =  (size // 2) - 1
    while p >= 0:
        siftdown(list, p, size)
        p -= 1

# sift down : parent에 child보다 큰 값이 오도록 swap
def siftdown(list, parentIdx, size):
    left = 2 * parentIdx + 1
    right = 2 * parentIdx + 2
    largestIdx = parentIdx
    if left <= size - 1 and list[left] > list[parentIdx]:
        largestIdx = left
    if right <= size - 1 and list[right] > list[largestIdx]:
        largestIdx = right
    if largestIdx != parentIdx:
        swap(list, parentIdx, largestIdx)
        siftdown(list, largestIdx, size)

def swap(list, firstIdx, secondIdx):
    tmp = list[firstIdx]
    list[firstIdx] = list[secondIdx]
    list[secondIdx] = tmp

def heapsort(list):
    size = len(list)
    heapify(list, size)
    end = size - 1
    while end > 0:
        swap(list, 0, end)
        siftdown(list, 0, end)
        end -= 1


arr = [8,5,3,1,9,6,0,7,4,2,5]
heapsort(arr)
print(arr)