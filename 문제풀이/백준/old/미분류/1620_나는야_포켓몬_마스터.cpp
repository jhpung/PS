#include <bits/stdc++.h>
using namespace std;

// 1 <= n, m <= 100,000;
int n, m;

unordered_map<int, string> m1;
unordered_map<string, int> m2;

string temp;
int tempi;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;

    for (int i = 1; i <= n; i++)
    {
        cin >> temp;
        m1.insert({i, temp});
        m2.insert({temp, i});
    }

    for (int i = 0; i < m; i++)
    {
        cin >> temp;

        tempi = atoi(temp.c_str());

        if (tempi)
        {
            cout << m1[tempi] << '\n';
        }
        else
        {
            if (m2[temp])
            {
                cout << m2[temp] << '\n';
            }
        }
    }
}