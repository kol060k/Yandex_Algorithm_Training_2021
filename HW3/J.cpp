#include <set>
#include <iostream>

using namespace std;

int main()
{
	int t, d, n;
	cin >> t >> d >> n;

	int x, y; // Показания навигатора
	int u_max = 0, u_min = 0, v_max = 0, v_min = 0; // Ограничения допустимой области в новых координатах
	for (int i = 0; i < n; i++) {
		cin >> x >> y;
		u_max = min(u_max + t, x + y + d);
		u_min = max(u_min - t, x + y - d);
		v_max = min(v_max + t, x - y + d);
		v_min = max(v_min - t, x - y - d);
	}

	// Теперь вычисляем возможные положения Мишы в старых координатах.
	// Для этого пробегаем по всем целым значениям u и v (так как если x и y целые, то и (x + y) и (x - y) тоже)
	// по ним находим x и y и отбираем те из них, что являются целыми (x = (u + v) / 2, y = (u - v) / 2)
	set<pair<int, int>> possible_coords;
	for (int u = u_min; u <= u_max; u++)
		for (int v = v_min; v <= v_max; v++)
			if ((u + v) % 2 == 0)
				possible_coords.insert(make_pair((u + v) / 2, (u - v) / 2));

	cout << possible_coords.size() << endl;
	for (auto it : possible_coords)
		cout << it.first << ' ' << it.second << endl;

	return 0;
}