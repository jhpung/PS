#include <bits/stdc++.h>
using namespace std;

int board[101][101] = {{
    0,
}};

int visited[101][101] = {{
    0,
}};

vector<int> result;

int m, n, k;
int lx, ly, rx, ry;

int cnt, cx, cy, dy, dx, nx, ny;

int dirs[4][2] = {
    {0, 1}, {1, 0}, {-1, 0}, {0, -1}};

int bfs(int y, int x)
{
    int cnt = 0;

    queue<pair<int, int>> q;

    q.push({y, x});

    while (!q.empty())
    {
        auto curr = q.front();
        q.pop();

        int cy = curr.first;
        int cx = curr.second;

        if (visited[cy][cx])
        {
            continue;
        }

        visited[cy][cx] = 1;
        cnt++;

        for (int i = 0; i < 4; i++)
        {
            dy = dirs[i][0];
            dx = dirs[i][1];
            ny = cy + dy;
            nx = cx + dx;

            if (ny < 0 || ny >= m || nx < 0 || nx >= n)
            {
                continue;
            }

            if (visited[ny][nx])
            {

                continue;
            }

            if (!board[ny][nx])
            {
                q.push(make_pair(ny, nx));
            }
        }
    }

    return cnt;
}

int main()
{
    vector<int> result;
    int num = 0;

    ios::sync_with_stdio(0);

    cin >> m >> n >> k;

    for (int i = 0; i < k; i++)
    {
        cin >> lx >> ly >> rx >> ry;

        for (int j = ly; j < ry; j++)
        {
            for (int k = lx; k < rx; k++)
            {
                board[j][k] = 1;
            }
        }
    }

    for (int y = 0; y < m; y++)
    {
        for (int x = 0; x < n; x++)
        {
            if (!board[y][x] && !visited[y][x])
            {
                num++;

                auto res = bfs(y, x);

                result.push_back(res);
            }
        }
    }

    sort(result.begin(), result.end());

    std::cout << num << '\n';

    for (auto iter = result.begin(); iter != result.end(); iter++)
    {
        std::cout << *iter << ' ';
    }
}