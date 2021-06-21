#include <vector>
#include <string>
#include <iostream>

using namespace std;

bool compare_word_dicts(vector<int> dict_1, vector<int> dict_2) {
	// Допустимые символы, по условию, 'A'-'Z', 'a'-'z'
	for (char c = 'A'; c <= 'Z'; c++) {
		if (dict_1[c] != dict_2[c])
			return false;
	}
	for (char c = 'a'; c <= 'z'; c++) {
		if (dict_1[c] != dict_2[c])
			return false;
	}
	return true;
}

int entry_number() {
	int g, s;
	cin >> g >> s;

	vector<int> g_dict(8 * 16);
	vector<int> s_dict(8 * 16);
	for (char c = 'A'; c <= 'Z'; c++) {
		g_dict[c] = 0;
		s_dict[c] = 0;
	}
	for (char c = 'a'; c <= 'z'; c++) {
		g_dict[c] = 0;
		s_dict[c] = 0;
	}

	// Составляем список символов слова g
	char c;
	for (int i = 0; i < g; i++) {
		cin >> c;
		g_dict[c] += 1;
	}

	// Список первых len(g) символов последовательности s
	string s_str;
	cin >> s_str;
	for (int i = 0; i < g; i++) {
		s_dict[s_str[i]] += 1;
	}
	
	// Каждый шаг сравниваем массивы символов g и текущих len(g) символов строки s, 
	// а затем сдвигаем окно и модифицируем массив символов для s
	int entry_num = 0;
	if (compare_word_dicts(g_dict, s_dict))
		entry_num += 1;
	for (int i = 0; i < s - g; i++) {
		s_dict[s_str[i]] -= 1;
		s_dict[s_str[i + g]] += 1;
		if (compare_word_dicts(g_dict, s_dict))
			entry_num += 1;
	}

	return entry_num;
}

int main()
{
	cout << entry_number();

	return 0;
}