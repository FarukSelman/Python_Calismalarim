class okul:
    #init fonksiyonu yapıcı fonksiyondur.Diğer fonksiyonlar üzerinde baskınlık kurar.

    def __init__(self,şube,öğretmen,bölüm,mevcut):
        self.şube = şube
        self.öğretmen = öğretmen
        self.bölüm = bölüm
        self.mevcut = mevcut

    def bilgileri_göster(self):
        print("-"*45)
        print("Sınıf Bilgileri")
        print("Şube:{}\nÖğretmen:{}\nBölüm:{}\nSınıf Mevcudu:{}".format(self.şube,self.öğretmen,self.bölüm,self.mevcut))
        print("-"*45)

    def öğretmen_adı(self):
        print("Öğretmen Adı:",self.öğretmen)

birinci_sınıf = okul("11-C","Tuncay Erol","Bilişim Teknolojileri","28")

birinci_sınıf.bilgileri_göster()

ikinci_sınıf = okul("12-B","Faruk Selman","Yazılım Mühendisliği","30")
ikinci_sınıf.bilgileri_göster()

ikinci_sınıf.öğretmen_adı()
