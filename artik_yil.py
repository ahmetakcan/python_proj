
sinir = 2200
for x in range(0, sinir):
    if x > 0:
        if (x % 4) == 0:
            if (x % 100) == 0:
                if (x % 400) == 0:
                    print(x ,"artık yıl")
                else:
                    print(x, "değil")
            else:
                print(x, "artık yıl")
        else:
            print(x, "değil")