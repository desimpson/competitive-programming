def operations(A, B, C, D):
    if B >= C * D:
        return -1

    count = 0
    while A > count * C * D:
        A += B
        count += 1
    return count


if __name__ == '__main__':
    A, B, C, D = map(int, input().split())
    print(operations(A, B, C, D))
