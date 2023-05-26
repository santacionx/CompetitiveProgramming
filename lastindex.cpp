#include <iostream>
using namespace std;
int rec(int a[], int size, int check)
{
    if (size == 0)
    {
        return -1;
    }
    int ans = rec(a + 1, size - 1, check);
    if (ans != -1)
    {
        return ans + 1;
    }
    if (a[0] == check)
    {
        return 0;
    }
    return -1;
}
int main()
{
    int a[6] = {1, 2, 2, 3, 4, 5};
    cout << rec(a, 6, 2);
}
