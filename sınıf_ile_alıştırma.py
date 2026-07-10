class okul:
    def __init__(self,şube,öğretmen,bölüm,mevcut,maaş):
        self.şube=şube
        self.öğretmen=öğretmen
        self.bölüm=bölüm
        self.mevcut=mevcut
        self.maaş=maaş

    def bilgileri_göster(self):  
        print("-"*45)
        print("Sınıf Bilgileri")
        print(f"Şube:{self.şube}\nÖğretmen:{self.öğretmen}\nBölüm:{self.bölüm}\nMevcut:{self.mevcut}")
        print("-"*45)

    def branç_değiş(self):
        yeni_branş = input("Lütfen Yeni Branşınızı Yazınız: ")
        print("***Eski Branş***",self.bölüm)
        self.bölüm = yeni_branş
        print("-"*45)
        print("Sınıf Bilgileri")
        print(f"Şube:{self.şube}\nÖğretmen:{self.öğretmen}\nBölüm:{self.bölüm}\nMevcut:{self.mevcut}")
        print("-"*45)

    def maaş_göster(self):
        print(f"{self.öğretmen} adlı öğretmenin maaşı {self.maaş} TL ")

class müdür(okul):
    def __init__(self, şube, öğretmen, bölüm, mevcut, maaş, kıdem):
        super().__init__(şube, öğretmen, bölüm, mevcut, maaş)
        self.kıdem = kıdem

    def bilgileri_göster(self):
        print("-" * 45)
        print("Sınıf Bilgileri")
        print(f"Şube:{self.şube}\nÖğretmen:{self.öğretmen}\nBölüm:{self.bölüm}\nMevcut:{self.mevcut}\nKıdem:{self.kıdem}")
        print("-" * 45)

    def zam_yap(self):
        print(f"Zam Ekranına Hoşgeldiniz Sayın {self.öğretmen}")
        zam_miktarı = int(input("Lütfen Zam miktarını TL cinsinden yazınız:"))
        self.maaş = int(self.maaş) + zam_miktarı
        print(f"{self.öğretmen} adlı öğretmenin maaşına {zam_miktarı} TL kadar zam yapıldı.")
        print(f"{self.öğretmen} adlı öğretmenin güncel maaşı {self.maaş} TL dir.")


# Yönetici Paneli İçin Döngü
while True:
    print("Seçim Yapınız")
    seçim_yap = input("1-Öğretmen Girişi\n2-Yönetici Girişi\n")

    if seçim_yap == "1":
        sınıf_adı = input("Lütfen Şube Numarası Giriniz: ")
        öğretmen_bilgisi = input("Lütfen Öğretmen İsmi Giriniz: ")
        bölüm_al = input("Lütfen Branşınızı Giriniz: ")
        mevcut = input("Sınıf Mevcudunu Giriniz: ")
        maas_miktarı = input("Maaş Miktarını Giriniz: ")
        sınıf_oluştur = input("Sınıf Oluşturunuz: ")

        sınıf_oluştur = okul(sınıf_adı, öğretmen_bilgisi, bölüm_al, mevcut, maas_miktarı)
        print("Sınıf Oluşturuldu...")

        tercih_yap = input("1-Bilgileri Göster\n2-Branş Değiştir\n3-Maaş Göster\n")
        if tercih_yap == "1":
            sınıf_oluştur.bilgileri_göster()

        elif tercih_yap == "2":
            sınıf_oluştur.branç_değiş()

        elif tercih_yap == "3":
            sınıf_oluştur.maaş_göster()

        else:
            print("Çıkış Yapıldı")
            break

    elif seçim_yap == "2":
        sınıf_adı = input("Lütfen Şube Numarası Giriniz: ")
        öğretmen_bilgisi = input("Lütfen Öğretmen İsmi Giriniz: ")
        bölüm_al = input("Lütfen Branşınızı Giriniz: ")
        mevcut = input("Sınıf Mevcudunu Giriniz: ")
        maaş_miktarı = input("Maaş Miktarını Giriniz: ")
        kıdem_al = input("Kıdem Yazınız: ")
        sınıf_oluştur = müdür(sınıf_adı, öğretmen_bilgisi, bölüm_al, mevcut, maaş_miktarı, kıdem_al)

        print("Yönetici Sınıfı Oluşturuldu")
        soru_sor = input("1-Bilgileri Göster\n2-Zam Yap\n")

        if soru_sor == "1":
            sınıf_oluştur.bilgileri_göster()

        elif soru_sor == "2":
            sınıf_oluştur.zam_yap()

        else:
            print("Çıkış Yapıldı")
            break
