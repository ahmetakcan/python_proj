# continue komutunu
# sadece "continue şartına uyan durumlar dışındaki" döngü şartlarını gerçekleştirmek için kullanırız.
# aşağıdaki örnekte de başlangıçtan sınıra kadar olan sayıları toplatıyoruz ancak dışında değerine yazdığımız
# değeri bu işleme sokmuyoruz.


baslangic = int(input("başlangıç için bir sayı belirleyin: "))
sinir = int(input("sınır için bir sayı belirleyin: "))
disinda = int(input("işlemde olmasını istemediğiniz sayıyı belirleyin: "))
x = 0


for i in range(baslangic, sinir + 1):
    if i == disinda:
        continue
    x = x + i

print(baslangic, "ile", sinir, "arasındaki", disinda, "dışındaki", "sayıların toplamı", x, "'dir." ) 