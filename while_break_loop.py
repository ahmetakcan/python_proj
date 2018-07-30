x = int(input("başlangıç: "))
i = x
sinir = int(input("sınırı belirleyiniz: "))

while i <= sinir:
    
    x = x + i
    i = i + 1 

print("sınıra kadar olan doğal sayıların toplamı ", x, "'dir.")


# tabi burada sınıra ihtiyaç yok
# çünkü sınırı while komutu sağlıyor.