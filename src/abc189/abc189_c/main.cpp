#include <iostream>
#include <algorithm>
#include <vector>

int main() {
    int n;
    std::vector<int> a;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        int l;
        std::cin >> l;
        a.push_back(l);
    }

    int ans = 0;
    for (int i = 0; i < n; i++) {
        int mn = 100000;
        for (int j = i; j < n; j++) {
            if (a[j] < mn) {
                mn = a[j];
            }
            ans = std::max(ans, (j - i + 1) * mn);
        }
    }

    std::cout << ans << "\n";
}