### Решение задачи J

Пробегаемся по каждой паре строк. Нам нужно найти `L`-й элемент отсортированной конкатенации двух массивов.

Вспомним, как проводится конкатенация двух отсортированных массивов:
- Для каждого массива заводится указатель, изначально указывающий на начало;
- Затем мы по одному берём меньших из двух элементов, на которые указывают указатели и двигаем соответствующий указатель вперёд.

Т.о. нам нужно с помощью бинпоиска по двум массивам найти положение двух указателей на пару массивов, которые соответствуют состоянию процесса конкатенации, когда выбирается элемент на L-ю позицию объединения. Тогда ответом будет меньшее из двух чисел, на которые указывают указатели.

Так как указатели соответствуют шагу, когда выбирается `L`-й элемент в конкатенацию, то их сумма должна быть равна `L-1`. Таким образом, будем реализовывать бинпоиск положения только одного из указателей. Второй будет однозначно определяться из условия на их сумму.

Осталось определить условие, которое будет проверяться при поиске. Поймём, как выглядит правильное положение указателей. В силу того, что объединение строится отсортированным, и элементы добавляются в него по возрастанию, получаем:
- `seq1[i-1] <= seq1[i] and seq1[i-1] <= seq2[j]`
- `seq2[j-1] <= seq2[j] and seq2[j-1] <= seq1[i]`

В нашем случае `i + j = L - 1`, а также не забываем, что обе последовательности и так отсортированы, имеем:
- `seq1[i-1] <= seq2[L-i-1]`
- `seq2[L-i-2] <= seq1[i]`

В таком случае `L`-м элементом объединённого массива будет `min(seq1[i], seq2[L-i-1])`. Если в обоих массивах подряд идут несколько одинаковых элементов, то значение `i` может определяться не однозначно, но это не играет роли.

Соответственно, алгоритм бинарного поиска на отрезке `[L, R]` выглядит, например, следующим образом:
```
m = (L + R) / 2
Если seq1[m - 1] <= seq2[L - m - 1], то сужаем отрезок до [L, m]
Иначе сужаем до [m + 1, R]
```