def tek_cift_kontrol(sayi):
    # Bir sayının 2 ile bölümünden kalan 0 ise çifttir, aksi halde tektir.
    if sayi % 2 == 0:
        return "Çift"
    else:
        return "Tek"

# Kullanım örneği:
num = int(input("Bir sayı girin: "))
print(f"Girilen sayı {tek_cift_kontrol(num)} bir sayıdır.")
