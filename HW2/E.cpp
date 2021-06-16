#include <vector>
#include <iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;
	int best_res = 0;
	int best_res_ind;
	vector<int> arr(n);
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
		if (arr[i] > best_res) {
			best_res = arr[i];
			best_res_ind = i;
		}
	}

	int best_possible_vasly = 0;
	for (int i = best_res_ind + 1; i < n - 1; i++) {
		if (arr[i] > best_possible_vasly && arr[i] % 10 == 5 && arr[i] > arr[i + 1])
			best_possible_vasly = arr[i];
	}

	int better_than_vasily = 0;
	for (int i = 0; i < n; i++)
		if (arr[i] > best_possible_vasly)
			better_than_vasily++;
	if (best_possible_vasly > 0)
		cout << better_than_vasily + 1;
	else
		cout << 0;
	return 0;
}