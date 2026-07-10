#Fonksiyonlar : Bir şeyi teker teker yapmak yerine fonksiyonla bir kere yapıp sınırsız kere kullanırız.def ile yazılır.
"""
def topla():
    a=int(input("Lütfen ilk sayıyı giriniz: "))
    b=int(input("Lütfen ikinci sayıyı giriniz: "))

    toplam=a+b
    print(toplam)


topla()

"""
#Fonksiyonlarda parametre kullanımı
"""
ad = input("Lütfen adınızı giriniz: ")
soyadı = input("Lütfen soyadınızı giriniz: ")
yaş = int(input("Lütfen yaşınızı giriniz: "))
meslek = input("Lütfen mesleğinizi giriniz: ")

print(f"Adınız: {ad}\nSoyadınız: {soyadı}\nYaşınız: {yaş}\nMesleğiniz: {meslek}")

"""
#Yukarıdakini fonksiyonlarla yapma

def kullanıcı_bilgileri(ad,soyad,yaş,meslek):

    print(f"Adınız: {ad}\nSoyadınız: {soyad}\nYaşınız: {yaş}\nMesleğiniz: {meslek}")
    print("*"*25)

kullanıcı_bilgileri("Faruk","Selman","21","Öğrenci")
kullanıcı_bilgileri("Tuncay","Erol","30","Öğretmen")
kullanıcı_bilgileri("Şiyar","Kaya","21","Fırıncı")

print("/"*30)

def kullanıcı_bilgileri2(adı,soyadı,yaşı,mesleki):

    print(f"Adınız: {adı}\nSoyadınız: {soyadı}\nYaşınız: {yaşı}\nMesleğiniz: {mesleki}")
    print("*"*25)

adı=input("Adınızı giriniz: ")
soyadı=input("Soyadınızı giriniz: ")
yaşı=input("Yaşınızı giriniz: ")
mesleki=input("Mesleğinizi giriniz: ")

kullanıcı_bilgileri2(adı,soyadı,yaşı,mesleki)
