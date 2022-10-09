import numpy as np
def F(n):
    print("Введите элементы матрицы (нажмите [enter] после каждого введенного элемента)")
    w = []
    if n == '1x2':
        a = np.array([[int(input()), int(input())]])
        w.append(a)
        aT = a.transpose()
        w.append(aT)
        return w
    elif n == '1x3':
        b = np.array([[int(input()), int(input()), int(input())]])
        w.append(b)
        bT = b.transpose()
        w.append(bT)
        return w
    elif n == '2x1':
        c = np.array([[int(input())], [int(input())]])
        w.append(c)
        cT = c.transpose()
        w.append(cT)
        return w
    elif n == '3x1':
        d = np.array([[int(input())], [int(input())], [int(input())]])
        w.append(d)
        dT = d.transpose()
        w.append(dT)
        return w
    elif n == '2x2':
        e = np.array([[int(input()), int(input())], [int(input()), int(input())]])
        w.append(e)
        eT = e.transpose()
        w.append(eT)
        return w
    elif n == '3x3':
        f = np.array([[int(input()), int(input()), int(input())], [int(input()), int(input()), int(input())], [int(input()), int(input()), int(input())]])
        w.append(f)
        fT = f.transpose()
        w.append(fT)
        return w


print("Выберите действие: Транспонирование, Умножение, Ранг")
q = str(input())
if q == 'Транспонирование':
    try:
        print("Введите размерность матрицы в английской раскладке клавиатуры:\n", "(1x2, 2x1, 1x3, 3x1, 2x2, 3x3)")
        n1 = str(input())
        ans = F(n1)
        print("Исходная матрица:\n", ans[0])
        print("Транспонированная матрица:\n", ans[1])
    except:
        print("Проверьте правильность введенных данных")
elif q == 'Умножение':
    try:
        print("Введите размерность первой матрицы в английской раскладке клавиатуры:\n")
        n2 = str(input())
        a1 = F(n2)[0]
        print("Введите размерность первой матрицы в английской раскладке клавиатуры:\n")
        n3 = str(input())
        a2 = F(n3)[0]
        ans = np.dot(a1, a2)
        print("Результат\n", ans)
    except:
        print("Проверьте корректность введенность данных и убедитесь в том, что число столбцов первой матрицы равно числу строк второй, после чего повторите запуск")
elif q == 'Ранг':
    try:
        print("Введите размерность матрицы в английской раскладке клавиатуры:\n", "(1x2, 2x1, 1x3, 3x1, 2x2, 3x3)")
        n4 = str(input())
        print("Ранг матрицы: ", np.linalg.matrix_rank(F(n4)[0]))
    except:
        print("Проверьте правильность введенных данных ")




