#include <bits/stdc++.h>
using namespace std;

long long a, b, c;
int main()
{
    cin >> a >> b >> c;

    for (int i = 0; i < b; i++)
    {
        a = (a * a) % c;
    }

    cout << a;
}