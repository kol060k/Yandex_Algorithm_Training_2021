#include <vector>
#include <string>
#include <iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;
	vector<int> arr(n);
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	int x;
	cin >> x;

	int diff = 5000;
	int best;
	for (int i = 0; i < n; i++) {
		if (abs(arr[i] - x) < diff) {
			best = arr[i];
			diff = abs(arr[i] - x);
		}
	}
	cout << best;

	return 0;
}