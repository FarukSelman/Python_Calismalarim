listeler=["Faruk","Selman","Yazılım",2500] #0.indisten başlar Faruk mesela 0.indis Selman 1.gibi

print(len(listeler))  #len uzunluğu verir yani kaç tane eleman olduğu 0.indis 1.indis 2.indis 3.indis toplamda 4 tane eleman var

print(listeler)  
print(listeler[1])  #kaçıncı indisi istersek kareli paranteze onu yazarız

listeler.append("Aydın") #.append listenin en sonuna eleman ekler
print(listeler) 

listeler[3]=2850  #burada istediğimiz indisin değerini değiştiriyoruz.
print(listeler)  

print(listeler[:2])  #listede kaç tane eleman yazdırmak istersek onu parantez içine : ile yazarız

listeler[:2]=["Mehmet","Arabacı"]  #listede kaç tane elemanı değiştirmek istersek onu yazarız
print(listeler)

listeler[0:3]=[]  #bu kaçıncı elemana kadar silmek istersek onu siliyor
print(listeler)