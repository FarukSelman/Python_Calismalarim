müşteri=20

if müşteri<18:
    print("Malesef yaşınız 18 den küçük sizin yaşınız:",müşteri)

else:
    print("Tebrikler yaşınız 18 den büyük yaşınız ise: ",müşteri)


müşteri_yaşı=int(input("Lütfen yaşınızı giriniz: "))

kabul_yaşı=18

if müşteri_yaşı<kabul_yaşı:
    print("Malesef yaşınız uygun değil: ",müşteri_yaşı)

else:
    print("Yaşınız uygun alışveriş yapabilirsiniz: ",müşteri_yaşı)


#  UYGULAMA 
süt_miktarı=int(input("Lütfen süt miktarını yazınız: "))
kaşar_peyniri_sınırı=11

if süt_miktarı < kaşar_peyniri_sınırı:
    print("Süt miktarınız Kaşar peynir için uygun değildir : " , süt_miktarı)
    print("Kaşar peyniri üretmek için gerekli olan süt miktarı : " ,(kaşar_peyniri_sınırı-süt_miktarı))

else:
    toplam_üretim=süt_miktarı/kaşar_peyniri_sınırı
    print(f"Toplam Üretim :{int(toplam_üretim)}")
