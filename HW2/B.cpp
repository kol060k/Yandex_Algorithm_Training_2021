#include <iostream>

using namespace std;

int main()
{
	int num, old_num;
	bool ascent = false; // Зарегистрирован ли рост на одном из значений
	bool descent = false; // Зарегистрирован ли спад на одном из значений
	bool constant = false; // Зарегистрировано ли постоянство на одном из значений
	int elem_num = 0;
	cin >> old_num;
	elem_num++;
	cin >> num;
	while (num != -2000000000) {
		elem_num++;
		if (num < old_num)
			descent = true;
		else if (num > old_num)
			ascent = true;
		else
			constant = true;
		old_num = num;
		cin >> num;
	}
	if (elem_num == 1)
		cout << "CONSTANT";
	else {
		if (ascent)
			if (descent)
				cout << "RANDOM";
			else if (constant)
				cout << "WEAKLY ASCENDING";
			else
				cout << "ASCENDING";
		else if (descent)
			if (constant)
				cout << "WEAKLY DESCENDING";
			else
				cout << "DESCENDING";
		else
			cout << "CONSTANT";
	}

	return 0;
}