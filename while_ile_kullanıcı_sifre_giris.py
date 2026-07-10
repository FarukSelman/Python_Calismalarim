sayı=1
while sayı<=10:
    print(sayı)
    sayı+=1

print("*"*50)

db_ka="admin"
db_ps=1234

while True:       #true dememizin sebebi ben istediğim kadar dönsün demek

    kullanıcı_adı=input("Lütfen kullanıcı adınızı giriniz: ")
    kullanıcı_ps=int(input("Lütfen şifrenizi giriniz: "))

    if db_ka==kullanıcı_adı and db_ps==kullanıcı_ps:
        print("Hoşgeldiniz :",kullanıcı_adı)
        break

    elif db_ka!=kullanıcı_adı and db_ps==kullanıcı_ps:
        print("Kullanıcı adınız hatalı")

    elif db_ka==kullanıcı_adı and db_ps!=kullanıcı_ps:
        print("Şifreniz hatalıdır")
        print("Şifreniz değiştirilsin mi? E/H :")
        cevap=input()
        if cevap=="E":
            print("Şifreniz değiştiriliyor...")
            yeni_şifre=int(input("Yeni şifrenizi giriniz: "))
            db_ps=yeni_şifre

    else:
        print("Kullanıcı adı ve şifre hatalıdır.")