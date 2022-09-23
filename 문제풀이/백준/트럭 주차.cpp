#include <bits/stdc++.h>
using namespace std;

int timeline[101] = {
    0,
};

int main()
{
    int a, b, c;

    int t1, t2;
    cin >> a >> b >> c;

    for (int i = 0; i < 3; i++)
    {
        cin >> t1 >> t2;

        for (int j = t1; j < t2; j++)
        {
            timeline[j]++;
        }
    }

    int sum = 0;
    for (int i = 0; i < 101; i++)
    {
        if (timeline[i] == 0)
        {
            continue;
        }

        if (timeline[i] == 1)
        {
            sum += a;
        }

        if (timeline[i] == 2)
        {
            sum += b * 2;
        }

        if (timeline[i] == 3)
        {
            sum += c * 3;
        }
    }

    cout << sum;
}