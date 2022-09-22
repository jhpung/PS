#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie();

    vector<int> heights;

    int tmp = 0;
    for (int i = 0; i < 9; i++)
    {
        cin >> tmp;

        heights.push_back(tmp);
    }

    sort(heights.begin(), heights.end());

    do
    {
        int sum = 0;

        for (int i = 0; i < 7; i++)
        {
            sum += heights[i];
        }

        if (sum == 100)
        {
            break;
        }
    } while (next_permutation(heights.begin(), heights.end()));

    for (int i = 0; i < 7; i++)
    {
        cout << heights[i] << "\n";
    }
}