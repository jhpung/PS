#include <bits/stdc++.h>
using namespace std;

int n, m;
int arr[15001];

int cnt;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >>
        n >> m;

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (arr[i] + arr[j] == m)
            {
                cnt++;
            }
        }
    }

    cout << cnt;
}