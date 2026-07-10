class galeri:
    araç_ismi="Ferari"
    km_değeri=9500
    renk="Kırmızı"

    def araba_özellikleri(self):         #dışarıdan değer aldığımız için self kullanmamız gerekiyor
        print(f"Araç İsmi:{self.araç_ismi}\nKm Değeri:{self.km_değeri}\nRenk Bilgisi:{self.renk}")

tuncay_otomativ = galeri()
tuncay_otomativ.araba_özellikleri()