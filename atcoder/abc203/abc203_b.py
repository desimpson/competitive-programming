def condominium_sum_v1(N, K):
    return sum([n * 100 + k for k in range(1, K + 1) for n in range(1, N + 1)])


def condominium_sum_v2(N, K):
    return N * K * (100 * (N + 1) + K + 1) // 2


def main():
    N, K = map(int, input().split())
    print(condominium_sum_v2(N, K))


if __name__ == '__main__':
    main()
