deneme= 8<10 and 11<12   #and --> ve demek iki koşulda doğru olmak zorundadır
print(deneme)

db_ps=124
db_ka="faruk"

kullanıcı_adı=input("Lütfen kullanıcı adınızı giriniz: ")
kullanıcı_sifre=int(input("Lütfen şifrenizi giriniz: "))

kontrol=db_ps==kullanıcı_sifre and db_ka==kullanıcı_adı

print(kontrol)

# or vardır o da veya anlamına gelir koşullardan sadece bir tanesi sağlanıyorsa yeterlidir.