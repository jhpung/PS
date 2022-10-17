#include <bits/stdc++.h>
using namespace std;

int n;

string patt;
string str;
string prefix;
string suffix;

vector<string> arr;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    cin >> patt;

    auto pos = patt.find('*');

    prefix = patt.substr(0, pos);
    suffix = patt.substr(pos + 1, patt.size());

    for (int i = 0; i < n; i++)
    {
        cin >> str;

        if (prefix.size() + suffix.size() > str.size())
        {
            cout << "NE\n";
        }
        else
        {
            if (prefix == str.substr(0, prefix.size()) && suffix == str.substr(str.size() - suffix.size()))
            {
                cout << "DA\n";
            }
            else
            {
                cout << "NE\n";
            }
        }
    }
}