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
	unordered_set<pair<int, int>, pair_hash> pairs;

	int n;
	cin >> n;

	int a, b;
	for (int i = 0; i < n; i++) {
		cin >> a >> b;
		if (a + b == n - 1 && a >= 0 && b >= 0)
			pairs.insert(make_pair(a, b));
	}

	cout << pairs.size();

	return 0;
}