def last_village(N, K, friends):
    friends.sort()
    for i in range(N):
        if friends[i][0] > K:
            break
        K += friends[i][1]
    return K


def main():
    N, K = map(int, input().split())
    friends = []
    for _ in range(N):
        a, b = map(int, input().split())
        friends.append((a, b))

    print(last_village(N, K, friends))


if __name__ == '__main__':
    main()
