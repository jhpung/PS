#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll a, b, c;

ll go(ll a, ll b)
{
    if (b == 1)
        return a % c;

    ll ret = go(a, b / 2);
    ret = (ret * ret) % c;

    if (b % 2)
        ret = (ret * a) % c;

    return ret;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> a >> b >> c;

    cout << go(a, b);
}