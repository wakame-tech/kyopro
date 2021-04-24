#include <iostream>
#include <vector>
#include <chrono>

int main() {
    std::vector<int> a {};
    for (int i = 0; i < 1e8; i++) {
        a.push_back(1);
    }

    int sum = 0;
    auto start = std::chrono::system_clock::now();
    for (int i = 0; i < 1e8; i++) {
        sum += a[i];
    }
    auto end = std::chrono::system_clock::now();
    auto msec = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
    std::cout << msec << "ms\n";
}