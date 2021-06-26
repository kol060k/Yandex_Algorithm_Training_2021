#include <vector>
#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	int n, m;
	cin >> n;
	vector<int> shirts(n);
	for (int i = 0; i < n; i++)
		cin >> shirts[i];
	cin >> m;
	vector<int> pants(m);
	for (int i = 0; i < m; i++)
		cin >> pants[i];

	int p1 = 0, p2 = 0;
	int min_diff = 20000001;
	int best_shirt, best_pants;
	while (p1 < n && p2 < m) {
		if (abs(shirts[p1] - pants[p2]) < min_diff) {
			min_diff = abs(shirts[p1] - pants[p2]);
			best_shirt = shirts[p1];
			best_pants = pants[p2];
		}
		if (shirts[p1] < pants[p2])
			p1++;
		else
			p2++;
	}

	cout << best_shirt << ' ' << best_pants;

	return 0;
}