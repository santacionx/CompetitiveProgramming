#include <iostream>
using namespace std;
int rec(int a[], int size)
{
    if (size == 0)
    {
        return 0;
    }
    return a[0] + rec(a + 1, size - 1);
}
int main()
{
    int a[5] = {1, 2, 3, 4, 5};
    cout << rec(a, 5);
}
