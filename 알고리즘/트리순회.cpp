#include <bits/stdc++.h>

using namespace std;

vector<int> adj[1004];
int visited[1005];

void postOrder(int here)
{
    if (visited[here])
    {
        return;
    }

    vector<int> curr = adj[here];

    if (curr.size() == 1)
    {
        postOrder(curr[0]);
    }
    if (curr.size() == 2)
    {
        postOrder(curr[0]);
        postOrder(curr[1]);
    }
    visited[here] = 1;
    cout << here << " ";
}
void preOrder(int here)
{
    if (visited[here])
    {
        return;
    }

    vector<int> curr = adj[here];

    visited[here] = 1;
    cout << here << " ";
    if (curr.size() == 1)
    {
        preOrder(curr[0]);
    }
    if (curr.size() == 2)
    {
        preOrder(curr[0]);
        preOrder(curr[1]);
    }
}
void inOrder(int here)
{
    if (visited[here])
    {
        return;
    }

    vector<int> curr = adj[here];

    if (curr.size() > 0)
    {
        inOrder(curr[0]);
    }
    visited[here] = 1;
    cout << here << " ";
    if (curr.size() > 1)
    {
        inOrder(curr[1]);
    }
}

int main()
{
    adj[1].push_back(2);
    adj[1].push_back(3);
    adj[2].push_back(4);
    adj[2].push_back(5);

    postOrder(1);
    memset(visited, 0, sizeof(visited));
    cout << '\n';
    preOrder(1);
    memset(visited, 0, sizeof(visited));
    cout << '\n';
    inOrder(1);
    
}