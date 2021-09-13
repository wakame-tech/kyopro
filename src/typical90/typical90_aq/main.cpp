#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <deque>

const int dx[4] = {1, 0, -1, 0};
const int dy[4] = {0, 1, 0, -1};

int bfs(std::vector<std::string> g, int w, int h, int sx, int sy, int gx, int gy) {
  int inf = 1000000;
  int costs[1000][1000][4];
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      for (int k = 0; k < 4; k++) {
        costs[i][j][k] = inf;
      }
    }
  }

  auto q = std::deque<std::pair<std::pair<int, int>, int>>();
  for (int i = 0; i < 4; i++) {
    costs[sy][sx][i] = 0;
    q.push_back(std::make_pair(std::make_pair(sx, sy), i));
  }

  while (!q.empty()) {
    auto u = q.front();
    int x = u.first.first, y = u.first.second, d = u.second;
    q.pop_front();

    for (int i = 0; i < 4; i++) {
      int nx = x + dx[i], ny = y + dy[i];
      if (nx < 0 || nx >= w || ny < 0 || ny >= h)
        continue;

      if (g[ny][nx] == '#')
        continue;

      int cost = costs[y][x][d] + (d != i ? 1 : 0);
      if (cost < costs[ny][nx][i]) {
        costs[ny][nx][i] = cost;
        std::pair<int, int> newpos = std::make_pair(nx, ny);
        if (d != i) {
          q.push_back(std::make_pair(newpos, i));
        } else {
          q.push_front(std::make_pair(newpos, i));
        }
      }
    }
  }

  int answer = inf;
  for (int i = 0; i < 4; i++) {
    answer = std::min(answer, costs[gy][gx][i]);
  }
  return answer;
}

int main() {
  int h, w, sy, sx, gy, gx;
  std::cin >> h >> w >> sy >> sx >> gy >> gx;
  sy--, sx--, gy--, gx--;

  std::vector<std::string> g(h);
  for (int i = 0; i < h; ++i) {
    std::cin >> g[i];
  }
  auto ans = bfs(g, w, h, sx, sy, gx, gy);
  std::cout << ans << std::endl;
}