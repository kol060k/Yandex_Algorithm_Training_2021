#include <vector>
#include <iostream>

using namespace std;

pair<int, int> shortest_segment(vector<int> trees, int k) {
	int L, R = 0;
	vector<int> trees_inside(k + 1); // Вектор, запоминающий кол-во деревьев каждого вида внутри отрезка. Работаем с ним от [1] до [k]
	// Такой способ инициализации заполняет вектор нулями!
	int trees_kinds_iside = 0; // Кол-во разных видов деревьев внутри. Отрезок нам подходит, если trees_kinds_iside == k
	int shortest = 250001;
	int L_best, R_best;
	for (L = 0; L < trees.size(); L++) {
		while (R < trees.size() && (L == R || trees_kinds_iside < k)) {
			if (trees_inside[trees[R]] == 0)
				trees_kinds_iside++;
			trees_inside[trees[R]]++;
			R++;
		}

		if (trees_kinds_iside == k && R - L < shortest) {
			shortest = R - L;
			L_best = L + 1; // Т.к. L нумерует с нуля
			R_best = R; // Тут всё норм, так как выше мы считаем, что граница R не включается в отрезок
		}

		if (trees_inside[trees[L]] == 1)
			trees_kinds_iside--;
		trees_inside[trees[L]]--;
	}
	return make_pair(L_best, R_best);
}

int main()
{
	int n, k;
	cin >> n >> k;
	vector<int> trees(n);
	for (int i = 0; i < n; i++)
		cin >> trees[i];

	pair<int, int> ans = shortest_segment(trees, k);
	cout << ans.first << ' ' << ans.second;

	return 0;
}