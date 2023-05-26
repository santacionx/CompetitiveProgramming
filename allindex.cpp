#include <iostream>
using namespace std;
int rec(int a[], int size, int check, int indices[])
{
    if (size == 0)
    {
        return 0;
    }
    int ans = rec(a + 1, size - 1, check, indices);
    for (int i = 0; i < ans; i++)
    {
        indices[i]++;
    }
    if (a[0] == check)
    {
        for (int i = ans - 1; i >= 0; i--)
        {
            indices[i + 1] = indices[i];
        }
        indices[0] = 0;
        ans++;
    }
    return ans;
}
int main()
{
    int a[5] = {1, 2, 3, 2, 3};
    int indices[5];
    int count = rec(a, 5, 2, indices);
    for (int i = 0; i < count; i++)
    {
        cout << indices[i] << " ";
    }
}
