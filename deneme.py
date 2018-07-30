

baslangic = int(input("başlangıç için bir sayı belirleyin: "))
sinir = int(input("sınır için bir sayı belirleyin: "))
disinda = int(input("işlemde olmasını istemediğiniz sayıyı belirleyin: "))
x = baslangic

for i in range(baslangic, sinir):
    if i == disinda:
        continue
    x = x + i
    i = i + 1 

print(baslangic, "ile", sinir, "arasındaki", disinda, "dışındaki", "sayıların toplamı", x, "'dir." ) 


"""onur adamdır"""