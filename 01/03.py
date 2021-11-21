# def square(length):
#     sm = (size - length) // 2
#     for i in range(length):
#         tab[sm + 0][sm + i] = 'X'
#     for i in range(length):
#         tab[sm + length - 1][sm + i] = 'X'
#     for i in range(length):
#         tab[sm + i][sm + 0] = 'X'
#     for i in range(length):
#         tab[sm + i][sm + length - 1] = 'X'


# def rec(r):
#     if r == 1:
#         tab[0][0] = 'X' # зная размер где центр
#     else:
#         square(r)
#         rec(r - 4)


# n = 3

# size = n*2 - 1
# tab = [
#     [' ' for col in range(size)] for row in range(size)
# ]

# rec(size)

# for row in tab:
#     print(*row)


#________________________________________________________________________

# import pymysql.cursors

# conn = pymysql.connect(
#     host='pgsha.ru', 
#     user='soft0027', 
#     password='ArMwliuG', 
#     db='soft0027_labrab',
#     port=35006,
#     cursorclass=pymysql.cursors.DictCursor)

# cur = conn.cursor()

# sql = 'SELECT * FROM 00'
# cur.execute(sql)
# rows = cur.fetchall()

# print(rows)

# conn.close()

# import pymysql

# db = pymysql.connect(host='localhost',user='root',passwd='yourpassword', database="bd")

# cursor = db.cursor()

# cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#________________________________________________________________________

# def line(i):
#     print(*[j * 0 for j in range(alpha[1])], sep=' ')


# def lines(i):
#     global beta
#     print(*[(i * beta) for i in range(alpha[1])], sep=' ')
#     beta *= 2


# alpha = list(map(int, input().split()))
# beta = 1

# [lines(i) if i > 0 else line(i) for i in range(alpha[0])]

#________________________________________________________________________

# alpha = list(map(int, input().split()))

# tab = [[0] * alpha[1] for i in range(alpha[0])]


# for r in range(alpha[0]):
#     for c in range(alpha[1]):
#         tab[r][c] = r * c

# for r in tab:
#     print(*r)

#________________________________________________________________________

# alpha = list(map(int, input().split()))

# A = [[0] * alpha[1] for i in range(alpha[0])]


# for row in A:
#     print(' '.join(list(map(str, row))))

#________________________________________________________________________

# tab = [[0] * col for i in range(row)]
# print(*tab)
# [print(*j) for j in tab]

# [print(*j) for j in [[0] * col for i in range(row)]]

#________________________________________________________________________

# alpha = list(map(int, input().split()))
# beta = 0

# tab = [[0] * alpha[1] for i in range(alpha[0])]

# for r in range(alpha[0]):
#     if r % 2 == 0:
#         for c in range(0, alpha[1], +1):
#             beta += 1
#             tab[r][c] = beta
#     else:
#         for c in range(alpha[1] - 1, -1, -1):
#             beta += 1
#             tab[r][c] = beta

# for r in tab:
#     print(' '.join(map(str, r)))

#________________________________________________________________________

# alpha = list(map(int, input().split()))
# beta = 0

# tab = [[0] * alpha[1] for i in range(alpha[0])]

# for c in range(alpha[1]):
#     if c % 2 == 0:
#         for r in range(0, alpha[0], +1):
#             beta += 1
#             tab[r][c] = beta
#     else:
#         for r in range(alpha[0] - 1, -1, -1):
#             beta += 1
#             tab[r][c] = beta

# for r in tab:
#     print(' '.join(map(str, r)))

#________________________________________________________________________


# alpha = list(map(int, input().split()))

# tab = [[0] * alpha[1] for i in range(alpha[0])]

# tab[0] = [(c + 1) for c in range(alpha[1])]

# for r in tab:
#     print(' '.join(map(str, r)))
