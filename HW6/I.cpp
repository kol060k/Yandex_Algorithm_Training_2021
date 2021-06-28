#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

bool is_diff_possible(vector<int> people, int n, int r, int c, int diff) {
	// Нужно проверить, сможем ли мы выделить R групп из C людей с макс. разницей в возрасте равной diff.
	// Для этого, очевидно, нужно отбирать в отсортированном первые встретившиеся непересекающиеся подходящий группы.
	// Будем пробегаться по массиву и считать отличия people[i] и people[i + c - 1].
	// Если разница меньше diff, запоминаем группу и идём далее.
	int cnt = 0;
	int i = 0;
	while (i + c - 1 < n) {
		if (people[i + c - 1] - people[i] <= diff) {
			// Если разница меньше diff, группа найдена, а следующая начинается с конца найденной
			cnt++;
			i += c;
		}
		else
			i++;
	}
	return (cnt >= r);
}

int bin_search_min_diff(vector<int> people, int n, int r, int c) {
	// Макс. возможное неудобство равно разности ростов самого низкого и самого высокого
	int L = 0;
	int R = people[n - 1] - people[0];
	while (L < R) {
		int m = (L + R) / 2;
		if (is_diff_possible(people, n, r, c, m))
			R = m;
		else
			L = m + 1;
	}
	return L;
}

int main()
{
	int n, r, c;
	cin >> n >> r >> c;
	vector<int> people(n);
	for (int i = 0; i < n; i++)
		cin >> people[i];
	// Отсортируем массив для использования далее
	sort(people.begin(), people.end());

	cout << bin_search_min_diff(people, n, r, c);

	return 0;
}