süper_lig={"Galatasaray":"63 puan","Fenerbahçe":"62 puan","Beşiktaş":"61 Puan"}

"""
süper_lig.setdefault("TranbzonSpor","100 puan") #setdefault  veri eklemeye yarar


takım_ekle=input("Takım giriniz: ")
puan_ekle=input("Puan ekle: ")

süper_lig.setdefault(takım_ekle,puan_ekle)

for isim,deger in süper_lig.items():
    print(isim,deger)


süper_lig.pop("Galatasaray")    #veri silmeye yarar
print(süper_lig)

"""
#veri güncellemesi yapacağız..while ile

while True:
    takım_ekle=input("Lütfen takım ekleyin: ")
    puan_ekle=int(input("Lütfen puan ekleyin: "))
    süper_lig.setdefault(takım_ekle,puan_ekle)

    for i,j in süper_lig.items():
        print(i,j)

    seçim = input("Çıkmak ister misiniz ? E/H: ").capitalize()
    if seçim =="E":
        print("Çıkış Yapıldı....")
        break
    else:
        pass   #pass döngünün devam etmesini sağlıyor
    
print("TAKIM LİSTESİ ")
print(süper_lig)
