for i in range(3):  #döngü 3 kere çalışması için
    şifre=input("Lütfen şifre belirleyiniz: ")
    if not şifre:  #not şifre girilmediği zaman boş kalmaması için
        print("Bu alan boş bırakılamaz") 
    elif len(şifre) in range(3,8):   #3 ve 8 karakter olması için
        print("Yeni şifreniz",şifre)
        break

    elif i==2:  #i==2 olmasının sebebi 0 1 2 toplam 3 kere olmasıdır
        print("Şifreyi 3 kere yanlış girdiniz,lütfen 15 dakika bekleyiniz")

    else:
        print("HATA! Şifreniz 8 karakterden uzun ya da 3 karakterden kısadır.")
