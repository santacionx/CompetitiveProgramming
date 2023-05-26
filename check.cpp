#include <iostream>
using namespace std;
bool rec(int a[], int size, bool check)
{
    if (size == 0)
    {
        return false;
    }
    if (a[0] == check)
    {
        return true;
    }
    return rec(a + 1, size - 1, check);
}
int main()
{
    int a[5] = {1, 2, 3, 4, 5};
    cout << rec(a, 5, 0);
}
