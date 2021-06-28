#include <algorithm>
#include <cmath>
#include <set>
#include <vector>
#include <iostream>

using namespace std;

int calc_triangles(vector<pair<int, int>> points, int n) {
	int cnt = 0;
	for (int p = 0; p < n; p++) {
		/*
		Найдём все равнобедренные треугольники с вершиной в выбранной точке i,
		то есть чтобы две равные стороны выходили из этой вершины.
		Строим отсортированный массив(квадратов) сторон для этой вершины,
		и затем в каждой группе сторон одинаковой длины попарно проверяем,
		не лежат ли отрезки на одной прямой(если не лежат, то треугольник построен).
		Равносторонние треугольники проверять не нужно, так как координаты всех точек - целые числа
		(равносторонних треугольников при таких условиях нет)
		*/
		// Для выбранной вершины создаём массив длин отрезков R_pi до каждой другой точки
		// Корень из длины стороны извлекать не будем, так как далее мы будем только проверять равенство сторон
		vector<long long> sides(n);
		set<pair<long long, long long>> prev_sides; // Массив, содержащий векторы от точки p, которые уже встречались
		int degenerated = 0; // Кол-во вырожденных треугольников (три точки на одной прямой)
		for (int i = 0; i < n; i++) {
			long long R_pi_x = points[p].first - points[i].first;
			long long R_pi_y = points[p].second - points[i].second;
			sides[i] = pow(R_pi_x, 2) + pow(R_pi_y, 2);
			if (prev_sides.count(make_pair(R_pi_x, R_pi_y)) > 0)
				degenerated++; // Если противопложный вектор встречался, получаем вырожденный треугольник
			else
				prev_sides.insert(make_pair(-R_pi_x, -R_pi_y));
		}
		// Сортируем его по длине R_ip
		sort(sides.begin(), sides.end());

		cnt -= degenerated;
		int L = 0, R = 1; // Указатели L и R нужны для ограничения набора [L, R) сторон одинаковой длины
		while (L < n) {
			while (R < n && sides[L] == sides[R])
				R++; // Ищем правую границу набора сторон одинаковой длины
			cnt += (R - L) * (R - L - 1) / 2; // Кол-во возможных треугольников, вырожденные выбросили ранее
			L = R; // После обработки набора сторон, переходим к следующему
			R++; 
		}	
	}
	return cnt;
}

int main()
{
	int n;
	cin >> n;

	vector<pair<int, int>> points(n);
	for (int i = 0; i < n; i++)
		cin >> points[i].first >> points[i].second;

	cout << calc_triangles(points, n);

	return 0;
}