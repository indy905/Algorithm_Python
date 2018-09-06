# 연습문제
# 1.1 1부터 n까지 연속한 숫자의 제곱의 합을 구하는 프로그램을 for 반복문으로 만들어 보세요.
# (입력 n = 10, 출력 385)

def square_sum_n(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i * i
    return s


print(square_sum_n(10))

# 1.2 1.1의 계산 복잡도는 O(1)과 O(n) 중 무엇일까요?
# O(n)

# 1.3 1부터 n까지 연속한 숫자의 제곱의 합을 구하는 공식은 n * (n + 1) * ( 2 * n + 1 ) // 6 으로 알려져있습니다.
# for 반복문 대신 공식을 이용하면 계산복잡도는 O(1)과 O(n)중 무엇이 될까요?
# O(1)

def square_sum_n_2(n):
    return n * (n + 1) * (2 * n + 1) // 6


print(square_sum_n_2(10))
