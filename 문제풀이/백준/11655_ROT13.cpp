#include <bits/stdc++.h>
using namespace std;

// A = 65
// a = 97
string s;
string ret;

char uppers[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
char lowers[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    getline(cin, s);

    for (auto it = s.begin(); it != s.end(); it++)
    {
        if (isalpha(*it))
        {
            if (isupper(*it))
            {
                ret += uppers[(*it - 'A' + 13) % 26];
            }
            else
            {
                ret += lowers[(*it - 'a' + 13) % 26];
            }
        }
        else
        {
            ret += *it;
        }
    }

    cout << ret;
}