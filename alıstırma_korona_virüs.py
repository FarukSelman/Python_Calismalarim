ateş_durumu=float(input("Lütfen ateş derecenizi giriniz: "))
öksürük = input("Öksürüğünüz var mı ? E/H:").lower
baş_ağrısı=input("Baş ağrınız var mı ? E/H:").lower
gün=int(input("Şikayetleriniz kaç gündür var ?:"))

if ateş_durumu>=39:
    if gün>=3:
        print("!!!Uyarı!!! Hastaneye Gidiniz.")
    else:
        print("Ateş durumunuz sınırda devam ederse en yakın sağlık kuruluşuna gidiniz...")

if (ateş_durumu>=39) and (öksürük=="e") and (baş_ağrısı=="e") and (gün>=3):
    print("!!!ACİL!!! Lütfen en yakın hastaneye gidiniz.")
    print("Durumunuz Olumlu Değil")

elif (öksürük=="e") or (baş_ağrısı=="e") or (gün>=3):
    print("*HATIRLATMA* Durumunuz bu şekilde devam ederse lütfen hastaneye gidiniz.")

else:
    print("Ateş durumunuz 39 üstüne çıkarsa lütfen hastaneye gidiniz ")