# TestZadanie
Условимся что точка А первый элемент массива, а точка Б последний элемент массива

Задача решена в тетради
На данном этапе:
- точка А переведена в начало координат
- Все точки смещенны относительно точки А
- все точки массива отсортированы по оси абцисс

<--- тут смещение точек относительно точки Б --->

- обнаружены все ближайшие точки вокруг А (обратная сторона) и добавлены в отдельный массив

осталось реализовать смещение точек относительно точки Б, для того чтобы отрезок АБ был на оси абцисс. Далее из рисунка "задание" можно понять в какой площади будет производиться отсеивание дальних точек
А на рисунке "задание2" нарисован процесс нахождения угла А, для того чтобы реализовать смещение точик Б на ось абцисс и смещения остальных точек.
Используется sin для нахождения угла А, зная угол А можно узнать новые координаты остальных точек
Зная то что будут выбраны лишь те точки которые находятся внутри площади неправильной фигуры, я собираюсь использовать логические и условные операторы, чтобы отсеять лишние, пример можете наблюдать в исполняемом файле

Я прекрасно понимаю что есть другое решение данной задачи, например методом наименьших квадратов, но я не успел реализовать и первый метод

Я понимаю, что я не успел в обознченный срок, но я отправлю полное решение данной задачи завтра до 00:00
