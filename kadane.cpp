#include <iostream>
using namespace std;

int kadane(int arr[], int size)
{
    int maxSoFar = 0;
    int maxEndingHere = 0;

    for (int i = 0; i < size; i++)
    {
        maxSoFar = maxSoFar + arr[i];
        if (maxEndingHere < maxSoFar)
        {
            maxEndingHere = maxSoFar;
        }
        if (maxSoFar < 0)
        {
            maxSoFar = 0;
        }
    }
    return maxEndingHere;
}

int main()
{
    int arr[] = {-2, -3, 4, -1, -2, 1, 5, -3};
    int size = sizeof(arr) / sizeof(arr[0]);

    int maxSum = kadane(arr, size);
    cout << "Maximum subarray sum: " << maxSum << endl;

    return 0;
}
