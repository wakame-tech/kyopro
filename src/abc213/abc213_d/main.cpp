#include <iostream>
#include <queue>
#include <functional>

std::vector<std::priority_queue<int, std::vector<int>, std::greater<int>>> g;
std::vector<bool> flags;

void dfs(int s) {
    flags[s] = true;
    std::cout << s + 1 << " ";

    while (!g[s].empty()) {
        int nex = g[s].top();
        g[s].pop();
        if (!flags[nex]) {
            dfs(nex);
            std::cout << s + 1 << ' ';
        }
    }
}

int main() {
    int n;
    std::cin >> n;
    g = std::vector<std::priority_queue<int, std::vector<int>, std::greater<int>>>(n);
    flags = std::vector<bool>(n, false);

    for (int i = 0; i < n; ++i) {
        g.push_back(std::priority_queue<int, std::vector<int>, std::greater<int>>());
    }

    for (int i = 0; i < n - 1; i++) {
        int a, b;
        std::cin >> a >> b;
        g[a - 1].push(b - 1);
        g[b - 1].push(a - 1);
    }

    dfs(0);
}