#include <bits/stdc++.h>
using namespace std;

int t, n;
string a, b;

int main()
{
    // ios::sync_with_stdio(false);
    // cin.tie(0);
    // cout.tie(0);

    cin >> t;

    while (t--)
    {
        map<string, int> _map;
        cin >> n;

        for (int i = 0; i < n; i++)
        {
            cin >> a >> b;

            _map[b]++;
        }

        int ret = 1;
        for (auto c : _map)
        {
            ret *= (c.second + 1);
        }

        ret--;

        cout << ret << '\n';
    }
}