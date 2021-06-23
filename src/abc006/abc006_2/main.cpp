#include <iostream>

int main() {
    int n;
    std::cin >> n;
    if (n <= 2) {
        std::cout << 0 << "\n";
    } else if (n <= 3) {
        std::cout << 1 << "\n";
    } else {
        int ans = 0;
        int pre = 0, prepre = 0, preprepre = 1;
        for (int i = 0; i < n - 2; i++) {
            ans = (pre + prepre + preprepre) % 10007;
            preprepre = prepre % 10007;
            prepre = pre % 10007;
            pre = ans % 10007;
        }
        std::cout << ans % 10007 << "\n";
    }
}