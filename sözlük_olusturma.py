sözlük={"Apple":"Elma","İsim":"Faruk","Telefon":"Apple"}  #bu bir sözlük örneğidir.3 değerlidir 6 değil
print(sözlük["Apple"])  #burada apple değeri yani çoktı olarak elma yazar.

print("*"*30)

for i in sözlük:
    print(i)   #boyle yaparsak içinde gezinir ilkini verir değeri vermez. Doğrusu:

print("*"*30)

for isim,değer in sözlük.items():
    print(isim,":",değer)
