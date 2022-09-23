#include <bits/stdc++.h>
using namespace std;

// 물에 잠긴경우 0 으로 마킹
int m[101][101];
int visited[101][101] = {
    {
        0,
    }};

int dy[] = {0, 1, 0, -1};
int dx[] = {1, 0, -1, 0};
int ret = 1;
int n;

int tmp = 0;

void dfs(int y, int x, int height)
{
    pair<int, int> curr;
    int ny, nx;

    stack<pair<int, int>> st;

    st.push({y, x});

    while (st.size())
    {
        curr = st.top();
        st.pop();

        visited[curr.first][curr.second] = 1;
        for (int i = 0; i < 4; i++)
        {
            ny = curr.first + dy[i];
            nx = curr.second + dx[i];

            if (ny < 0 || ny >= n || nx < 0 || nx >= n)
            {
                continue;
            }

            if (visited[ny][nx])
            {
                continue;
            }

            if (m[ny][nx] > height)
            {
                st.push({ny, nx});
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie();

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> m[i][j];
        }
    }

    for (int d = 1; d < 101; d++)
    {
        fill(&visited[0][0], &visited[0][0] + 101 * 101, 0);
        int cnt = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (!visited[i][j] && m[i][j] > d)
                {
                    dfs(i, j, d);
                    cnt++;
                }
            }
        }

        ret = max(ret, cnt);
    }

    cout << ret;

    return 0;
}