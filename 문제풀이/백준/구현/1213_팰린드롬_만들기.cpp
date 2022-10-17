#include <bits/stdc++.h>
using namespace std;

string s;
string ret;

int cnt[200];
int flag = 0;
char mid;

int main()
{

    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> s;

    for (char a : s)
    {
        cnt[a]++;
    }

    for (int i = 'Z'; i >= 'A'; i--)
    {
        if (cnt[i] & 1)
        {
            mid = i;
            flag++;
            cnt[i]--;
        }
        if (flag == 2)
            break;
        for (int j = 0; j < cnt[i]; j += 2)
        {
            ret = (char)i + ret;
            ret += (char)i;
        }
    }

    if (flag == 2)
    {
        cout << "I'm Sorry Hansoo" << '\n';
    }
    else
    {
        if (mid)
        {
            ret.insert(ret.begin() + ret.size() / 2, mid);
        }
        cout << ret;
    }
}