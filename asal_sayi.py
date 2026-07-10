import math

def asal_mi(sayi):
    if sayi <= 1:
        return False
    if sayi == 2:
        return True
    if sayi % 2 == 0:
        return False  # 2 hariç çift sayılar asal olamaz

    # Verimlilik için sadece sayının kareköküne kadar olan tek sayıları kontrol ediyoruz
    sinir = int(math.sqrt(sayi)) + 1
    for i in range(3, sinir, 2):
        if sayi % i == 0:
            return False
            
    return True

# Kullanım örneği:
num = int(input("Bir sayı girin: "))
if asal_mi(num):
    print(f"{num} bir asal sayıdır.")
else:
    print(f"{num} bir asal sayı değildir.")
