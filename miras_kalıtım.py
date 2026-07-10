class okul:

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

    def branç_değiş(self):
        yeni_branş = input("Lütfen Yeni Branşınızı Yazınız: ")
        print("***Eski Branş***",self.bölüm)
        self.bölüm = yeni_branş
        print("-"*45)
        print("Sınıf Bilgileri")
        print(f"Şube:{self.şube}\nÖğretmen:{self.öğretmen}\nBölüm:{self.bölüm}\nMevcut:{self.mevcut}")
        print("-"*45)

class müdür(okul):          #müdür sınıfı okuldan miras alıyor.Onun için parantezin içine yazıyoruz
       #pass                 #pass diğer sınıftaki işlemleri yapıyor.
    print("Yönetici Paneli")   
    def __init__(self,şube,öğretmen,bölüm,mevcut,kıdem):
        #self.şube=şube
        #self.öğretmen=öğretmen
        #self.bölüm=bölüm
        #self.mevcut=mevcut
        #self.kıdem=kıdem
        #Yukarıdakileri super diyerek tekrar yazmadan alabiliriz.
        super().__init__(şube,öğretmen,bölüm,mevcut)
        self.kıdem=kıdem

    def bilgileri_göster(self):  
        print("-"*45)
        print("Yönetici Paneli")
        print(f"Şube:{self.şube}\nÖğretmen:{self.öğretmen}\nBölüm:{self.bölüm}\nMevcut:{self.mevcut}\nKıdem:{self.kıdem}")
        print("-"*45)

yönetici = müdür("11-A","Faruk","Yazılım","15","Patron")
yönetici.bilgileri_göster()



