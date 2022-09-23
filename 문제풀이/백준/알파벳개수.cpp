#include <bits/stdc++.h>
using namespace std;

unordered_map<char, int> mp;

int main()
{
    string input;

    cin >> input;

    for (int i = 0; i < input.size(); i++)
    {
        if (mp.find(input[i]) == mp.end())
        {
            mp.insert({input[i], 1});
        }
        else
        {
            mp[input[i]] += 1;
        }
    }

    for (int i = 97; i < 123; i++)
    {
        int count = 0;
        if (mp.find((char)i) == mp.end())
        {
            cout << count << " ";
            continue;
        }

        cout << mp.find(i)->second << " ";
    }
}