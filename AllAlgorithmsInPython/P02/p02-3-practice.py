# 2-1 숫자 n개를 리스트로 입력받아 최소값을 구하는 프로그램을 만들어 보세요.

def find_min(a):
    n = len(a)
    min = a[0]
    for i in range(1, n):
        if min > a[i]:
            min = a[i]
    return min


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_min(v))
