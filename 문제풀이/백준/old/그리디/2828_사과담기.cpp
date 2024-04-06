#include <bits/stdc++.h>
using namespace std;

int n, m, j, tmp, ret = 0;
int pos = 1;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m >> j;

    for (int i = 0; i < j; i++)
    {
        cin >> tmp;

        if (tmp < pos)
        {
            ret += abs(pos - tmp);
            pos -= (pos - tmp);
        }
        else if (tmp >= pos + m)
        {
            ret += abs(pos + (m - 1) - tmp);
            pos += abs(pos + (m - 1) - tmp);
        }
    }

    cout << ret;
}
