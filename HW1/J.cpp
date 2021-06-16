#include <iostream>

using namespace std;

void solve_system_zeros_line(double c, double d, double e, double f) {
	// 0x + 0y = e
	// cx + dy = f
	if (e == 0) {
		if (c == 0 && d == 0)
			if (f == 0)
				cout << 5;
			else
				cout << 0;
		else if (c == 0)
			cout << 4 << ' ' << f / d;
		else if (d == 0)
			cout << 3 << ' ' << f / c;
		else
			cout << 1 << ' ' << -c / d << ' ' << f / d;
	}
	else
		cout << 0;
}

void solve_system_zeros_column1(double b, double d, double e, double f) {
	// 0x + by = e, b != 0
	// 0x + dy = f, d != 0
	if (e / b == f / d)
		cout << 4 << ' ' << e / b;
	else
		cout << 0;
}

void solve_system_zeros_column2(double a, double c, double e, double f) {
	// ax + 0y = e, a != 0
	// cx + 0y = f, c != 0
	if (e / a == f / c)
		cout << 3 << ' ' << e / a;
	else
		cout << 0;
}

void solve_system_zeros_diag(double a, double d, double e, double f) {
	// ax + 0y = e, a != 0
	// 0x + dy = f, d != 0
	cout << 2 << ' ' << e / a << ' ' << f / d;
}

bool solve_system_with_two_zeros(double a, double b, double c, double d, double e, double f) {
	if (a == 0 && b == 0)
		solve_system_zeros_line(c, d, e, f);
	else if (c == 0 && d == 0)
		solve_system_zeros_line(a, b, f, e);
	else if (a == 0 && c == 0)
		solve_system_zeros_column1(b, d, e, f);
	else if (b == 0 && d == 0)
		solve_system_zeros_column2(a, c, e, f);
	else if (c == 0 && b == 0)
		solve_system_zeros_diag(a, d, e, f);
	else if (a == 0 && d == 0)
		solve_system_zeros_diag(c, b, f, e);
	else
		return false;
	return true;
}

int main()
{
	// ax + by = e
	// cx + dy = f
	double a, b, c, d, e, f;
	cin >> a >> b >> c >> d >> e >> f;
	
	// Проверим, является ли наша система тривиальной с двумя нулями
	bool res = solve_system_with_two_zeros(a, b, c, d, e, f);
	// Если нет, используем метод Гаусса для сведения её к таковому виду
	if (!res) {
		if (a != 0 && d != 0) {
			// Проверим, вдруг система стала тривиальной
			a -= c * b / d;
			e -= f * b / d;
			b = 0;
			res = solve_system_with_two_zeros(a, b, c, d, e, f);
			// Если нет, ещё одна итерация Гаусса
			if (!res) {
				f -= e * c / a;
				c = 0;
				solve_system_with_two_zeros(a, b, c, d, e, f);
			}
		}
		else { // Тогда точно b != 0 и c != 0
			b -= d * a / c;
			e -= f * a / c;
			a = 0;
			res = solve_system_with_two_zeros(a, b, c, d, e, f);
			if (!res) {
				f -= e * d / b;
				d = 0;
				solve_system_with_two_zeros(a, b, c, d, e, f);
			}
		}
	}
	return 0;
}