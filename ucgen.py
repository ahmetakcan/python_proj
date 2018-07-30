birinci_kenar = 2
ikinci_kenar = 5
ucuncu_kenar = 6
u = (birinci_kenar + ikinci_kenar + ucuncu_kenar) / 2
A = ((u * (u - birinci_kenar) * (u - ikinci_kenar) * (u - ucuncu_kenar)) ** float(0.5))

if u < birinci_kenar:
    print("BU BİR ÜÇGEN BİLE DEĞİL AMINA KOYUM")
    if u < ikinci_kenar:
        print("BU BİR ÜÇGEN BİLE DEĞİL AMINA KOYUM")
        if u < ucuncu_kenar:
            print("BU BİR ÜÇGEN BİLE DEĞİL AMINA KOYUM")
else:
    if birinci_kenar > 0:
        if ikinci_kenar > 0:
            if ucuncu_kenar > 0:
                print("kenar uzunlukları", birinci_kenar, ikinci_kenar, ucuncu_kenar, "olan üçgenin alanı")
                print("u= ", u)
                print("Alan= ", A, "'dır.")    
            else:
                print("şaka mı!!!")
        else:
            print("ciddi olamazsın!!!")
    else:
        print("bunu bana yaptırma!!!")

