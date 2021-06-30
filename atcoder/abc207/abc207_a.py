def maximum_sum(A, B, C):
    return max(A + B, A + C, B + C)


if __name__ == '__main__':
    A, B, C = map(int, input().split())
    print(maximum_sum(A, B, C))
