def faktoriyel_hesapla(sayi):
    if sayi < 0:
        return "Negatif sayıların faktöriyeli tanımlı değildir."
    
    sonuc = 1
    # 1'den girilen sayıya kadar döngü ile çarpım yapılır
    for i in range(1, sayi + 1):
        sonuc *= i
        
    return sonuc

# Kullanım örneği:
num = int(input("Faktöriyeli alınacak sayıyı girin: "))
print(f"{num}! = {faktoriyel_hesapla(num)}")
