tr = "şçöğüıŞÇÖĞÜİ"

parola = input("Sisteme giriş için bir parola belirleyin: ")

parolalar = set("abc")

if set(tr) & set(parola):
    print("Parolanızda Türkçe harfler kullanmayın!")

elif set(parola) & set(parolalar):
    print("bu şifre kullanılıyor.")

else:
    print("Parolanız kabul edildi!")
    parolalar.add(input)


    



# PROGRAMI İLK ÇALIŞTIRDIĞIMDA PAROLA İSTİYOR, GİRDİĞİM PAROLA UYGUN DEĞİLSE TEKRARLATIYOR
# ANCAK UYGUNSA GİRDİĞİM PAROLAYI "PAROLALAR" A YAZDIRAMIYORUM. 
# parolalar.add(input) ile kaydetmesini sağladım ama burada da sıkıntı önce ekliyor sonra kontrol ediyor. 
# yani ne girersem gireyim bu şifre kullanılıyor sonucu veriyor. 
# döngü kullanmadığım için break de kullanamıyorum. haliyle işlemi durdurmuyor ve ekledikten sonra şartları
# tekrar kontrol ediyor. nasıl durdurabileceğimi bulamadım. sanırım başka bir yöntem kullanmam gerekiyor.