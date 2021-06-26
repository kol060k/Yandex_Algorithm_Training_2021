#include <vector>
#include <iostream>

using namespace std;

long long calc_variants(vector<int> monuments, int n, int min_dist) {
	int L, R = 0;
	long long variants = 0;
	for (L = 0; L < n; L++) {
		// Интересное замечание по условию ниже! Если R == n, то R < n == false и всё, что стоит после && не вычисляется,
		// тем самым не вылазит ошибка выхода за границы массива при обращении monuments[R]
		while (R < n && (L == R || monuments[R] - monuments[L] <= min_dist))
			R++;
		variants += n - R;
	}
	return variants;
}

int main()
{
	int n, r;
	cin >> n >> r;
	vector<int> monuments(n);
	for (int i = 0; i < n; i++)
		cin >> monuments[i];

	cout << calc_variants(monuments, n, r);

	return 0;
}