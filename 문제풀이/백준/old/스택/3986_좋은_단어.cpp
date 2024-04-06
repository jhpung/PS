#include <bits/stdc++.h>
using namespace std;

int n;
int cnt = 0;
string s;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        stack<char> st;
        cin >> s;

        for (auto ch : s)
        {
            if (st.size())
            {
                if (st.top() == ch)
                {
                    st.pop();
                    continue;
                }
            }
            st.push(ch);
        }
        if (!st.size())
        {
            cnt++;
        }
    }

    cout << cnt;
}