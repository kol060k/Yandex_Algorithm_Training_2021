#include <cmath>
#include <string>
#include <map>
#include <iostream>

using namespace std;

void conduct_operation(map<string, int>* client_dict, string operation) {
	string name, name2;
	int sum, p;
	if (operation == "DEPOSIT") {
		cin >> name >> sum;
		if ((*client_dict).count(name) == 0)
			(*client_dict)[name] = 0;
		(*client_dict)[name] += sum;
	}
	else if (operation == "WITHDRAW") {
		cin >> name >> sum;
		if (!(*client_dict).count(name))
			(*client_dict)[name] = 0;
		(*client_dict)[name] -= sum;
	}
	else if (operation == "BALANCE") {
		cin >> name;
		if ((*client_dict).count(name) > 0)
			cout << (*client_dict)[name] << endl;
		else 
			if (name.length() > 0)  // Небольшой костыль - защита от того, что последняя операция повторяется 2 раза (какие-то особенности ввода?)
				cout << "ERROR" << endl;
	}
	else if (operation == "TRANSFER") {
		cin >> name >> name2 >> sum;
		if (!(*client_dict).count(name))
			(*client_dict)[name] = 0;
		if (!(*client_dict).count(name2))
			(*client_dict)[name2] = 0;
		(*client_dict)[name] -= sum;
		(*client_dict)[name2] += sum;
	}
	else if (operation == "INCOME") {
		cin >> p;
		// Для каждого созданного счёта (account, пара (client, money)) проводим операцию
		for (map<string, int>::iterator account = (*client_dict).begin(); account != (*client_dict).end(); account++) {
			if (account->second > 0)
				account->second += trunc(account->second * p / 100);
		}
	}
}

int main()
{
	map<string, int> client_dict;
	
	string operation;
	while (cin.peek() != EOF) {
		cin >> operation;
		if (operation.length() == 0) { // Если ввод окончен, но в конце есть паразитные пробелы
			cout << "1" << endl;
			return 0;
		}
		else
			conduct_operation(&client_dict, operation);
	}

	return 0;
}