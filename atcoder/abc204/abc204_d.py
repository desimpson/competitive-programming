def main():
    N = int(input())
    T = list(map(int, input().split()))
    total = sum(T)
    dp = [False] * (total + 1)
    dp[0] = True
    for t in T:
        print(f'    t = {t}')
        for i in range(total + 1)[::-1]:
            print(f'        i = {i}')
            if dp[i]:
                print(f'            dp[i] = {dp[i]}')
                dp[i + t] = True
                print(f'            dp[i + t] = {dp[i + t]}')
    print()
    print(dp)

    ans = total
    for i in range(total + 1):
        if dp[i]:
            tmp = max(i, total - i)
            ans = min(ans, tmp)


if __name__ == '__main__':
    main()
