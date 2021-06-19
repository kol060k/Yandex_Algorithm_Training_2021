#include <string>
#include <map>
#include <iostream>

using namespace std;

int main()
{
	map<string, string> dict;
	int n;
	cin >> n;

	string word1, word2;
	for (int i = 0; i < n; i++) {
		cin >> word1 >> word2;
		dict[word1] = word2;
		dict[word2] = word1;
	}

	cin >> word1;
	cout << dict[word1];

	return 0;
}