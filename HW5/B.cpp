#include <vector>
#include <iostream>

using namespace std;

int sums(vector<int> numbers, int n, int k) {
	// Рассматриваем отрезки [L,R)
	int L = 0, R = 0;
	int count = 0;
	int sum = 0;
	for (L = 0; L < n; L++) {
		while (R < n && (L == R || sum < k)) {
			sum += numbers[R];
			R++;
		}
		if (sum == k)
			count++;
		sum -= numbers[L];
	}
	return count;
}

int main()
{
	int n, k;
	cin >> n >> k;
	vector<int> numbers(n);
	for (int i = 0; i < n; i++)
		cin >> numbers[i];

	cout << sums(numbers, n, k);

	return 0;
}