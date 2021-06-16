#include <algorithm>
#include <vector>
#include <unordered_set>
#include <iostream>

using namespace std;

int main()
{
	unordered_set<int> set_A, set_B;
	int n1, n2;
	cin >> n1 >> n2;
	int k;
	for (int i = 0; i < n1; i++) {
		cin >> k;
		set_A.insert(k);
	}
	for (int i = 0; i < n2; i++) {
		cin >> k;
		set_B.insert(k);
	}

	vector<int> intersection;
	for (int elem : set_A) {
		if (set_B.count(elem) > 0)
			intersection.push_back(elem);
	}
	sort(intersection.begin(), intersection.end());

	cout << intersection.size() << endl;
	for (auto it = intersection.begin(); it != intersection.end(); ++it)
		cout << *it << ' ';
	cout << endl;

	vector<int> diff_A;
	for (int elem : set_A) {
		if (set_B.count(elem) == 0)
			diff_A.push_back(elem);
	}
	sort(diff_A.begin(), diff_A.end());

	cout << diff_A.size() << endl;
	for (auto it = diff_A.begin(); it != diff_A.end(); ++it)
		cout << *it << ' ';
	cout << endl;

	vector<int> diff_B;
	for (int elem : set_B) {
		if (set_A.count(elem) == 0)
			diff_B.push_back(elem);
	}
	sort(diff_B.begin(), diff_B.end());

	cout << diff_B.size() << endl;
	for (auto it = diff_B.begin(); it != diff_B.end(); ++it)
		cout << *it << ' ';

	return 0;
}