class Okul:

    def __init__(self,şube,öğretmen,bölüm,mevcut):
        self.şube=şube
        self.öğretmen=öğretmen
        self.bölüm=bölüm
        self.mevcut=mevcut

    def bilgileri_göster(self):  #dışarıdan veri kullanacağımız için self yazıyoruz.
        print("-"*45)
        print("Sınıf Bilgileri")
        print(f"Şube:{self.şube}\nÖğretmen:{self.öğretmen}\nBölüm:{self.bölüm}\nMevcut:{self.mevcut}")
        print("-"*45)

    def branş_değiştir(self):
        yeni_branş = input("Lütfen Yeni Branşınızı Yazınız: ")
        print("***Eski Branş***",self.bölüm)
        self.bölüm = yeni_branş
        print("-"*45)
        print("Sınıf Bilgileri")
        print(f"Şube:{self.şube}\nÖğretmen:{self.öğretmen}\nBölüm:{self.bölüm}\nMevcut:{self.mevcut}")
        print("-"*45)
"""
sınıf_1 =Okul("11-C","Tuncay Erol","Bilişim","45")
sınıf_1.bilgileri_göster()
sınıf_1.branş_değiştir()

"""
while True:
    sınıf_adı = input("Lütfen Şube Numarası Giriniz: ")
    öğretmen_bilgisi=input("Lütfen İsminizi Giriniz: ")
    bölüm_al=input("Lütfen Branşınızı Giriniz: ")
    mevcut=input("Sınıf Mevcudunu Giriniz: ")

    yeni_sınıf=Okul(sınıf_adı,öğretmen_bilgisi,bölüm_al,mevcut)

    print("HOŞGELDİNİZ")
    seçim=input("Branş Değiştirmek için lütfen 1 tuşuna basınız:")
    if seçim=="1":
        yeni_sınıf.branş_değiştir()
    else:
        print("İşlem bitti...")
        break