deneme = "faruk selman Beşiktaş"

deneme=deneme.split()  #split metodu kelimeleri ayırıyor.

print(deneme)
print(deneme[0])

deneme1="faruk,selman,Beşiktaş"
deneme1=deneme1.split(",")   #aralarına virgül koyduğumuz için splitin içine de virgül koymak gerekiyor
print(deneme1)

tarih="21/01/2004"
tarih=tarih.split("/")
print(tarih)
print(tarih[1])

veri_al=input("Lütfen parçalanacak kelimeleri yazınız: ")
for i in veri_al:
    print(i)   # bu bütün kelimeleri alt alta yazar

veri_al1=input("Lütfen parçalanacak kelimeleri yazınız: ")
for i in veri_al.split():
    print(i,end="")   #bu yan yana yazar   # end="" birleştir anlamına geliyor. 


veri_al2=input("Lütfen parçalanacak kelimeleri yazınız: ")
for i in veri_al.split():
    print(i[0],end="")   # bu verilerin ilk harflerini alır.
