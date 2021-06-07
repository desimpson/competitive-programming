def nuts(A):
    return sum(map(lambda n: n - 10, filter(lambda n: n > 10, A)))


def main():
    _, A = int(input()), list(map(int, input().split()))
    print(nuts(A))


if __name__ == '__main__':
    main()
