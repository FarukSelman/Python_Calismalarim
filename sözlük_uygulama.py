tel_rehberi=dict()  #içi boş bir sözlük olşturuldu

def tel_no_ekle(x):
    print("***NUMARA EKLEME EKRANINA HOŞGELDİNİZ***")
    numara_isim_al=input("Lütfen Kayıt Edilecek Kişinin Adını Giriniz: ")
    numara_no_al=int(input("Lütfen Telefon Numarası Giriniz: "))

    x = tel_rehberi.setdefault(numara_isim_al,numara_no_al)

    print(f"{numara_isim_al}' adlı kişi telefon listesine eklendi...")

def tel_rehber_göster(x):
    print("Rehbere Hoşgeldiniz")
    kişi_sayısı=len(x)
    print(f"Rehberdeki kayıtlı kişi sayısı: {kişi_sayısı}")

    for i,j in x.items():
        print(i,":",j)

def no_sil(x):
    print("Kişi Silme Ekranına Hoşgeldiniz")
    silinecek_kişi=input("Silinecek Kişiyi Yazınız: ")
    x = tel_rehberi.pop(silinecek_kişi)
    print(f"{silinecek_kişi}' adlı kişi telefon listesinden silindi...")


while True:
    print("***HOŞGELDİNİZ***")
    print("***Seçim Yapınız***")
    seçim_yap=int(input("1-Ekle\n2-Sil\n3-Rehberi Gör\n4-Çıkış\n"))

    if seçim_yap==1:
        tel_no_ekle(tel_rehberi)
    
    elif seçim_yap==2:
        no_sil(tel_rehberi)

    elif seçim_yap==3:
        tel_rehber_göster(tel_rehberi)

    elif seçim_yap==4:
        print("Çıkış yapılıyorrr...")
        break

    else:
        print("Lütfen uygun tuşlara basınız!!!")

