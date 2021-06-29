#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

void medians_of_concatenations(vector<vector<int>> seqs, int n, int l) {
	// Пояснение в файле J_solution.md
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			int left = 0;
			int right = l - 1;
			while (left < right) {
				int m = (left + right + 1) / 2;
				if (seqs[i][m-1] <= seqs[j][l - m - 1])
					left = m;
				else
					right = m - 1;
			}
			cout << min(seqs[i][left], seqs[j][l - left - 1]) << endl;
		}
	}
}

int main()
{
	int n, l;
	cin >> n >> l;
	vector<vector<int>> seqs(n);
	for (int i = 0; i < n; i++) {
		vector<int> temp(l);
		for (int j = 0; j < l; j++)
			cin >> temp[j];
		seqs[i] = temp;
	}

	medians_of_concatenations(seqs, n, l);

	return 0;
}