#include <unordered_set>
#include <iostream>

using namespace std;

struct pair_hash {
	std::size_t operator()(const std::pair<int, int> & v) const {
		return v.first * 37 + v.second;
	}
};

int main()
{
	unordered_set<pair<int, int>, pair_hash> coords;

	int t, d, n;
	cin >> t >> d >> n;

	coords.insert(make_pair(0, 0));
	int x, y;
	for (int i = 0; i < n; i++) {
		unordered_set<pair<int, int>, pair_hash> new_coords;
		cin >> x >> y;
		for (int j = x - d; j <= x + d; j++)
			for (int k = y - (d - abs(x - j)); k <= y + (d - abs(x - j)); k++)
				for (auto it = coords.begin(); it != coords.end(); ++it)
					if (abs(j - it->first) + abs(k - it->second) <= t) {
						new_coords.insert(make_pair(j, k));
					}
		coords = new_coords;
	}

	cout << coords.size() << endl;
	for (auto it = coords.begin(); it != coords.end(); ++it)
		cout << it->first << ' ' << it->second << endl;

	return 0;
}