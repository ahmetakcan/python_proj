print("0 ile 1000 arasındaki asal sayılar")

for x in range(1,1000):
    if x > 1:
        for y in range(2,x):
            if (x % y) == 0:
                break
        else:
                print(x)