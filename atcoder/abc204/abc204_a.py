def hand(x, y):
    return x if x == y else {0, 1, 2}.difference({x, y}).pop()


def main():
    x, y = map(int, input().split())
    print(hand(x, y))


if __name__ == '__main__':
    main()
