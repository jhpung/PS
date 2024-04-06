#include <bits/stdc++.h>
using namespace std;

int n;
string tmp;
vector<string> m;
int cnt = 0;

struct Point
{
    int x, y;
};

string recursion(Point lt, Point rb)
{
    string ret = "";
    char tmp = '\0';

    if (lt.x == rb.x && lt.y == rb.y)
    {
        return ret += m[lt.y][lt.x];
    }

    // cout << '(' << lt.y << ',' << lt.x << ')' << '(' << rb.y << ", " << rb.x << ')' << endl;

    for (int cy = lt.y; cy < rb.y; cy++)
    {
        for (int cx = lt.x; cx < rb.x; cx++)
        {
            if (tmp == '\0')
            {
                tmp = m[cy][cx];
            }
            else
            {
                if (tmp != m[cy][cx])
                {

                    // 왼쪽 위
                    // 왼쪽 위 점은 그대로, 오른쪽 아래 점은 2분의 1씩
                    // 2, 2
                    // 4, 4
                    // 2, 2
                    // 2, 2
                    Point half = {
                        .y = (lt.y + rb.y) / 2,
                        .x = (lt.x + rb.x) / 2};

                    ret += recursion({.y = lt.y,
                                      .x = lt.x},
                                     half);
                    // 오른쪽 위
                    // 왼쪽 위 점은 x위치만 2분의 1위치로, 오른쪽 위 점은 y랑 위치만 2분의 1위치로
                    ret += recursion({.y = lt.y, .x = half.x}, {.y = half.y, .x = rb.x});
                    // 왼쪽 아래
                    // 왼쪽 위 점은 y위치만 2분의 1위치로, 오른쪽 아래 점은 x위치만 2분의 1위치로,
                    ret += recursion({.y = half.y,
                                      .x = lt.x},
                                     {.y = rb.y, .x = half.x});
                    // 오른쪽 아래
                    // 왼쪽 위 점은 y위치랑 x위치 둘 다 2분의 1 위치로,
                    ret += recursion(half, {.y = rb.y, .x = rb.x});
                    return '(' + ret + ')';
                }
            }
        }
    }
    return ret += tmp;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        m.push_back(tmp);
    }

    Point lt = {.x = 0,
                .y = 0};

    Point rb = {.x = n,
                .y = n};

    cout << recursion(lt, rb);
}