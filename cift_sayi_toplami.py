# 0-10 arasındaki çift sayıların toplamı

y = 0

for i in range(10):

    x = (i % 2)

    if x == 0:
        y += i
# (y += i) ile (y = y + i) aynı şeyler

        print(y)