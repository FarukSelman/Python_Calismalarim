import random

print(random.random()) # rastgele sayılar üretir

a=random.random()  # 0 ile 1 arasında üretir
print(round(a*10 , 2)) #virgülden sonraki 2 basamağı gelir bide çarpı 10 yaptığımız için 0. olmaz
b=random.random()
print(round(b*10 , 1)) 

c=random.uniform(1.5 , 2.5) #1.5 ile 2.5 arasında rastgele sayı üretir.
print(c)

d=random.randint(20,100)  #20 ile 100 arasında tam sayılar verir. randint sayesinde
print(d)


liste=["Faruk","Selman","Yazılım","Aydın","Beşiktaş"]

e=random.choice(liste)  #random.choice oluşturduğumuz listeden rastgele veri seçer.
print(e)

random.shuffle(liste)  #.shuffle  listeyi karıştırır
print(liste)

f=random.sample(liste,2)  #listeden rastgele 2 tane numune verir.
print(f)
