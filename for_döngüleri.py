liste=["faruk","selman","aydın","yazılım mühendisliği"]

for i in liste:
    print(i)

for sayılar in range(20):  #range fonksiyonu 0 dan başlayarak sayılar yazar içine yazdığımız dahil değil
    print(sayılar)

for sayılar2 in range(5,14):
    print(sayılar2)       #range içine iki tane sayı yazdık onların arasındaki sayıları yazar. ilk sayı dahil olur ama ikinci sayı olmaz


deneme="faruk"

for i in deneme:
    print(i)   #denemedeki yani faruktaki bütün harfleri tek tek geziyor  
    
deneme1="faruk"

for i in deneme1:
    print(deneme1)  #deneme1 =faruk olduğundan ve 5 harfli olduğundan 5 kere faruk yazıyor
    