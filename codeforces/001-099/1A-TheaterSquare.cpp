#include <iostream>

unsigned long long numStones(unsigned long long n, unsigned long long m,
                        unsigned long long a) {
    unsigned long long x, y;
    x = y = 1;
    if (a < n)
        x = n / a + (n % a != 0);
    if (a < m)
        y = m / a + (m % a != 0);
    return x * y;
}

int main() {
    unsigned long long n, m, a;
    std::cin >> n >> m >> a;
    std::cout << numStones(n, m, a) << std::endl;
    return 0;
}
