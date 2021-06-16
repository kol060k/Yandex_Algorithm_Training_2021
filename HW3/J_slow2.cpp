#include <set>
#include <iostream>

using namespace std;

struct pair_hash {
	std::size_t operator()(const std::pair<int, int> & v) const {
		return v.first * 37 + v.second;
	}
};

int main()
{
	set<pair<int, int>> coords;

	int t, d, n;
	cin >> t >> d >> n;

	coords.insert(make_pair(0, 0));
	int x, y;
	int min_x, max_x, min_y, max_y;
	for (int i = 0; i < n; i++) {
		set<pair<int, int>> new_coords;
		cin >> x >> y;
		for (auto it = coords.begin(); it != coords.end(); ++it)
			if (abs(it->first - x) + abs(it->second - y) <= d + t) {
				min_x = max(x - d, it->first - t);
				max_x = min(x + d, it->first + t);
				for (int j = min_x; j <= max_x; j++) {
					min_y = max( y - (d - abs(x - j)), it->second - (t - abs(it->first - j)) );
					max_y = min( y + (d - abs(x - j)), it->second + (t - abs(it->first - j)) );
					for (int k = min_y; k <= max_y; k++)
						if (abs(j - it->first) + abs(k - it->second) <= t) {
							new_coords.insert(make_pair(j, k));
						}
				}
			}
		coords = new_coords;
	}

	cout << coords.size() << endl;
	for (auto it = coords.begin(); it != coords.end(); ++it)
		cout << it->first << ' ' << it->second << endl;

	return 0;
}