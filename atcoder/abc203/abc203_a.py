def remaining_or_zero(a, b, c):
    if a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return 0


def main():
    a, b, c = map(int, input().split())
    print(remaining_or_zero(a, b, c))


if __name__ == '__main__':
    main()
