def palindrom_mu(veri):
    # Veriyi stringe çevirip küçük harfe dönüştürüyoruz (büyük/küçük harf duyarlılığını kaldırmak için)
    temiz_veri = str(veri).lower().replace(" ", "")
    
    # [::-1] ifadesi stringi tamamen tersine çevirir
    return temiz_veri == temiz_veri[::-1]

# Kullanım örneği:
girdi = input("Kontrol edilecek metin veya sayıyı girin: ")
if palindrom_mu(girdi):
    print(f"'{girdi}' bir palindromdur.")
else:
    print(f"'{girdi}' bir palindrom değildir.")
