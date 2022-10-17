#include <bits/stdc++.h>
using namespace std;

int n, k;
int temp;
int acc[100004];
int ret = -10000001;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> k;

    for (int i = 1; i <= n; i++)
    {
        cin >> temp;
        acc[i] = acc[i - 1] + temp;
    }

    for (int i = k; i <= n; i++)
    {
        ret = max(ret, acc[i] - acc[i - k]);
    }

    cout << ret;
}
