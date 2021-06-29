#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

void medians_of_concatenations(vector<vector<int>> seqs, int n, int l) {
	// Решение задачи абсолютно аналогично задаче J из этого же д/з,
	// отличается только способ построения массива пос-тей.
	// Пояснения по решению см. в файле J_solution.md
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

	int x, d, a, c, m;
	for (int i = 0; i < n; i++) {
		// Усложнённый по сравнению с задачей J способ получения последовательностей
		vector<int> temp(l);
		cin >> x >> d >> a >> c >> m;
		temp[0] = x;
		for (int j = 1; j < l; j++) {
			temp[j] = temp[j - 1] + d;
			d = (a * d + c) % m;
		}
		seqs[i] = temp;
	}

	medians_of_concatenations(seqs, n, l);

	return 0;
}