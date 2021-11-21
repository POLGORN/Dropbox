Начало
===
> ### Единственная истинная мудрость — в осознании, что мы по сути ничего не знаем.
Пример работы со строками
---
---
```Py
n = int(input())
a = [i for i in range(1, n + 1)]
print(a) #Просто список
print(a[-1]) #Последний элемент
print(a[:]) #Просто список
print(a[::2]) #Выбирает каждый второй элемент
print(a[1::2]) #Выбирает каждый второй элемент только начинает сделав 1 шаг вперёд
print(a[::-1]) #Читает наоборот
print(a[5:]) #ВЫРЕЗАЕТ первые 5 всё остальное ОСТАВЛЯЕТ
print(a[:5]) #ОСТАВЛЯЕТ первые 5 всё остальное ВЫРЕЗАЕТ
print(a[-2:1:1]) #Я не знаю чё это

# Разбивает по-символьно
s = 'Hdfs Tutorial'
b = [c for c in s]
print(b)
```
---
---
> ### Если хочешь учиться, будь готов считаться дураком и тупицей.
Пример работы со списком
---
---
```Py
# Делает список
n = int(input())
p = [i for i in range(1, (n ** 2) + 1)]
print(p)

# Делит с.
def split(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr = arr[size:]
     arrs.append(arr)
     return arrs
a = split(p, n)
print(a)

# Печатает с. со скобками
j = 0
for i in a:
    print(a[0 + j])
    j += 1

# Печатает с. без скобок
for row in a:
    print(' '.join(map(str, row)))

# Печатает с. без скобокно и в строку
print(str(p)[1:-1])

# Печатает первый список списка 
for i in a[0]:
    print(i,end = ' ')

# Делит с. только не выебисто
print(list(zip(*[iter(p)] * 2)))
print(list(zip(*[iter(p)] * 3)))

# Выводит по-элементно
for row in p:
    print(' '.join(map(str, row)))


```

---
---
> ### Мудрость — это знать, насколько мало мы знаем.
Примеры мелких функций
---
---
* Функция + генератор = круто
```Py
def get(x):
    return x ** 2

lst = [get(i) for i in range(10)]
print(lst)
```
---
* Паралельный счёт
```Py
def par():
    a = []
    b = []
    for i, j in zip(range(10,20), range(1,10)):
        a.append(i)
        b.append(j)
    return a, b
print(par())
```
---
* Выдает время на обработку кода
```Py
from datetime import timedelta
def time():
    start_time = time.monotonic()
    end_time = time.monotonic()
    alpha = timedelta(seconds=end_time - start_time)
    return alpha
time()
```
* Проверяет чётность/нечётность
```Py
def even_odd():
    n = int(input())
    if n % 2 == 0:
        print('True')
    else:
        print('False')
```
* Из 2-х чисел показывает большее
```Py
def maxxx():
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a > b:
        print(a)
    else:
        print(b)
```
---
---
> ### Сначала скажи себе, каким ты хочешь стать, а потом делай, что должен.
Примеры мелких программ
---
---

* Пишет в файле 2/1 + 2/3 + 4/3 + 4/5 + 6/5 + 6/7 +...
```Py
my_file = open("some.txt", "w")
n = int(input())
a, b = 2, 1
for i in range(1, n+1):
    if i % 2 == 0:
        y = a / b
        my_file.write(str(y) + '\n')
        a += 2
    else:
        z = a / b
        my_file.write(str(z) + '\n')
        b += 2
my_file.close()
```
---
* Читает этот файл 
```Py
my_file = open("some.txt")
my_string = my_file.read()
print("Было прочитано:")
print(my_string)
my_file.close()
```
---
* Делает пирамидку из X высотой n (пожалуйста не задавай n = 1000)
```Py
n = int(input())
m = n - 1
for i in range(0, n):
    print(' ' * m + 'X' * i + 'X' + 'X' * i)
    m += -1
```
---
* Дай бог понять как это работает
```Py
import math
g = int(input())
q = float(input())
x = math.pi/180 * g
p = 1; z = 1; sin_x = 0; step = q + 1
while abs(step) > q:
    step = z * (x**p / math.factorial(p))
    p += 2; z = -z; sin_x += step
print('sin = %.3f' % sin_x)
```
---
* Крепость из крестиков
```Py
# # Делает стенку из X-X-... размером n*n
def task02():
    n = int(input())
    a = str()
    f = str()
    b = c
    d = e
    for i in range (1, n + 1):
        if b % 2 == 0:
            a += '-'
            b += 1
        else:
            a += 'X'
            b += 1
    for i in range (1, n + 1):
        if d % 2 == 0:
            f += '-'
            d += 1
        else:
            f += 'X'
            d += 1
    for i in range (1, n + 1):
        if k == 1:
            print((a + '\n') * n)
        else:
            w = 1
            if w % 2 == 0:
                print(f)
                w += 1
            else:
                print(a)
                w += 1

# # Задаёт конфигурации
c = 1
e = 2
k = 2
task02()
```
---
* Крепость из крестиков которые уважают шахматы
```Py
# # Делает стенку из X-X-... размером n*n и переворачивает чётные строки
def tek():
    n = int(input())
    m = ''
    a = [i for i in range(1, (n ** 2) + 1)]
    for i in a:
        if i % 2 == 0:
            m += '-'
        else:
            m += 'X'
    b = m[:n]
    c = m[1:n + 1]
    if k == 1:
        print((b + '\n') * n) 
    if k != 1:
        for i in range(1, n + 1):
            if i % 2 == 0:
                print(c)
            else:
                print(b)

# # Конфигурация
k = 2
tek()
```
---
* Дай список, а он even = много чётных, odd = много нечётных, equal = равное
```Py
n = input()
m = n.split()
a = ''
b = ''
for i in m:
    if int(i) % 2 == 0:
        a += '1'
    else:
        b += '1'
if len(a) > len(b):
    print('even')
if len(a) < len(b):
    print('odd')
if len(a) == len(b):
    print('equal')
```
---
* Девочка с пальцами
```Py
n = int(input())
m = 0
p = 1
for a in range(0, n):
    if p == 1:
        while n != 0 and m < 5:
            m += 1
            n -= 1
        p += 1
    if p == 2:
        while n != 0 and m > 1:
            m -= 1
            n -= 1
        p -= 1
print(m)
```
---
* Пишешь кол-во чисел, пишешь сами числа, получаешь наименьшее кратное 3
```Py
def check(x):
    return x % 10 == 3
row = int(input())
lst = [int(input()) for n in range(row)]
print(min(filter(check,lst)))
```
---
* Тоже самое только короче
```Py
row = int(input())
print(min(filter(lambda x: x % 10 == 3,[int(input()) for n in range(row)])))
```
---
* Дай номер линии - получи линию файла
```Py
which = input('Which package would you like?: ')
with open('input.txt') as f:
    i = 1
    for line in f:
        if i == (int(which)):
            break
        i += 1
print (line)
```
---
---
* Убить тех кто заслужит сего 
```Py
# Много строк
list1 = ['1', '2', '3',]
list2 = ['1', '3',]
for item in list2:
    if item in list1:
        list1.remove(item)
print(list1)

# Норм строк
list1 = ['Вася', 'Петя', 'Маша', 'Саша']   
list2 = ['Вася', 'Петя'] 
list3= list(set(list1)-set(list2))  
print(list3)  

# Вообще малюсенько
z = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
print([z[i] for i in range(len(z)) if i == z.index(z[i])])

my_list = [3, 5, 2, 1, 4, 4, 1]
opt = [item for item in set(my_list) if my_list.count(item) > 1]
print(opt)
```
---
* Ход коня v.1
```Py
alpha = input()
beta = alpha.split('-')
gamma = []

def check(right_steps, delta):
    gamma = ''
    for item in right_steps:
        if item == delta:
            gamma += '1'
        else:
            gamma += '0'
    if '1' in gamma:
        print('YES')
    else:
        print('NO')

def steps_of_the_horse(i, omega):
    global delta
    k = row.index(omega)
    print(i + k)
    print(i, k)
    right_steps = []
    configure = 0
    for item in range(4):
        if configure == 0:
            k -= 2
            i += 1
            right_steps.append(str(i) + str(k))
            i -= 2
            right_steps.append(str(i) + str(k))
            configure += 1
            continue  
        if configure == 1:
            k += 4
            right_steps.append(str(i) + str(k))
            i += 2
            right_steps.append(str(i) + str(k))
            configure += 1
            continue  
        if configure == 2:
            i += 1
            k -= 1
            right_steps.append(str(i) + str(k))
            k -= 2
            right_steps.append(str(i) + str(k))
            configure += 1
            continue  
        if configure == 3:
            i -= 4
            right_steps.append(str(i) + str(k))
            k += 2
            right_steps.append(str(i) + str(k))
            continue  
    
    for nums in right_steps:
        for num in nums:
            if num > str(8) or num < str(1):
                right_steps.remove(nums)

    check(right_steps, delta)
    print(right_steps)

# C4-F4
# A1-F4

print(beta[0])
delta = ''

for i in range(8, 0, -1):
    row = []
    pos_begin = 65
    pos_end = 73
    for pos in range(pos_begin, pos_end):
        omega = chr(pos) + str(i)
        row.append(omega)
        k = row.index(omega)
        if beta[0] == omega:
            print(str(i) + str(k))
            steps_of_the_horse(i, omega)
        if beta[1] == omega:
            delta = str(i) + str(k)
        

    print(row)
print(delta)
```
---
* Ход коня v.2
```Py
chess_board = [
    ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8'],
    ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
    ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
    ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
    ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
    ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
    ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
    ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']
]

# print(chess_board[1][1]) # B7
# print(chess_board[4][4]) # E4
# print(chess_board[3][2]) # C5
# print(chess_board[2][3]) # D6

# C2-G6
# C4-E3

def find_and_assign(beta):
    global i, j
    for row in chess_board:
        print('row = ' + str(chess_board.index(row)))
        for column in row:
            print(row.index(column))
            if str(beta[0]) == column:
                delta = column
                i, j = chess_board.index(row), row.index(delta)
                print(i, j)
                right_step_or_not(i, j)  


def right_step_or_not(i, j):
    gamma = []
    clean_gamma = []
    gamma.append(horizontally())
    gamma.append(vertically())
    print(gamma)
    print(beta[1])
    for item in gamma:
        for i in item:
            clean_gamma.append(i)
    print(clean_gamma)
    if beta[1] in clean_gamma:
        print('YES')
    else:
        print('NO')



def horizontally():
    try:
        a1, b1 = chess_board[i + 1][j + 2], chess_board[i - 1][j + 2]
        c1, d1 = chess_board[i + 1][j - 2], chess_board[i - 1][j - 2]
        return a1, b1, c1, d1
    except:
        try:
            a1, b1 = chess_board[i + 1][j + 2], chess_board[i - 1][j + 2]
            return a1, b1
        except:
            c1, d1 = chess_board[i + 1][j - 2], chess_board[i - 1][j - 2]
            return c1, d1

def vertically():
    try:
        a2, b2 = chess_board[i + 2][j + 1], chess_board[i + 2][j - 1]
        c2, d2 = chess_board[i - 2][j + 1], chess_board[i - 2][j - 1]
        return a2, b2, c2, d2
    except:
        try:
            a2, b2 = chess_board[i + 2][j + 1], chess_board[i + 2][j - 1]
            return a2, b2
        except:
            c2, d2 = chess_board[i - 2][j + 1], chess_board[i - 2][j - 1]
            return c2, d2



alpha = input()
beta = alpha.split('-')

find_and_assign(beta)
```
---
* Cмещаем коды символов для сокрытия
```Py
key = 9
line = 'Привед Медвед...'
lst = [ord(smb)+key for smb in line]
print(lst)

result = ''
for item in lst:
    result += chr(item)
print(result)
```
---
* Функции кодирования и декодирования
```Py
def code(line, key):
    return ''.join([chr(ord(smb)+key) for smb in line])


def decode(line, key):
    return ''.join([chr(ord(smb)-key) for smb in line])


key = 9
line = 'Привед Медвед...'

print(line)
line_code = code(line, key)
print(line_code)
line_decode = decode(line_code, key)
print(line_decode)
```
---
* Одна функция для шифрования
```Py
def code(line, key, z=1):
    return ''.join([chr(ord(smb)+z*key) for smb in line])


key = 9
line = 'Привед Медвед...'

print(line)
line_code = code(line, key)
print(line_code)
line_decode = code(line_code, key, -1)
print(line_decode)
```
---
* Способ кодирования XOR
```Py
a = 5 # исходный код символа
k = 2 # ключ для шифрования

c = a ^ k # закодировать

print("%7s" % bin(a)[2:])
print("%7s" % bin(k)[2:])
print("%7s" % bin(c)[2:])

print("%7d" % c)

d = c ^ k # декодировать

print("%7s" % bin(d)[2:])
print("%7d" % d)
```
---
* Одна функция для шифрования XOR
```Py
def code(line, key):
    return ''.join([chr(ord(smb)^key) for smb in line])


key = 999
line = 'Привед Медвед...'

print(line)
line_code = code(line, key)
print(line_code)
line_decode = code(line_code, key)
print(line_decode)
```
---
---
> ### Мудрость — это знать, насколько мало мы знаем.
Примеры
---
* 
```Py

```
---
* 
```Py

```
---
* 
```Py

```
---
* 
```Py

```
---
* 
```Py

```
---
* 
```Py

```
---
* 
```Py

```
---
* 
```Py

```
---