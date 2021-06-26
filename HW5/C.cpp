#include <vector>
#include <iostream>

using namespace std;

vector<int> calc_up_prefixsums(vector<int> coords, int n) {
	// Вычисляем сумму подъёмов на отрезках [0, i] если идти слева направо
	vector<int> prefsums(n);
	prefsums[0] = 0;
	for (int i = 1; i < n; i++)
		if (coords[i] > coords[i - 1])
			prefsums[i] = prefsums[i - 1] + (coords[i] - coords[i - 1]);
		else
			prefsums[i] = prefsums[i - 1];
	return prefsums;
}

vector<int> calc_down_prefixsums(vector<int> coords, int n) {
	// Вычисляем сумму подъёмов на отрезках [i, n-1] если идти справа налево
	vector<int> prefsums(n);
	prefsums[n - 1] = 0;
	for (int i = n - 2; i >= 0; i--)
		if (coords[i] > coords[i + 1])
			prefsums[i] = prefsums[i + 1] + (coords[i] - coords[i + 1]);
		else
			prefsums[i] = prefsums[i + 1];
	return prefsums;
}

int main()
{
	int n, m, tmp;
	cin >> n;
	vector<int> coords(n);
	for (int i = 0; i < n; i++)
		cin >> tmp >> coords[i];

	vector<int> prefsums_to_right = calc_up_prefixsums(coords, n);
	vector<int> prefsums_to_left = calc_down_prefixsums(coords, n);

	cin >> m;
	int start, stop;
	vector<int> answers(m);
	for (int i = 0; i < m; i++) {
		cin >> start >> stop;
		if (start <= stop)
			answers[i] = prefsums_to_right[stop - 1] - prefsums_to_right[start - 1];
		else
			answers[i] = prefsums_to_left[stop - 1] - prefsums_to_left[start - 1];
	}

	for (int i = 0; i < m; i++)
		cout << answers[i] << endl;

	return 0;
}