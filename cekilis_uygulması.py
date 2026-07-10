import random
import time

kullanıcılar=list()

def kullanıcı_ekle(x):
    print("-"*30)
    print("Kullanıcı Ekleme Ekranına Hoşgeldiniz")
    ekle=input("Lütfen Eklenecek Kullanıcıyı Yazınız: ")
    kullanıcılar.append(ekle)
    input("Devam Etmek İçin Enter Tuşuna Basınız.")

def kullanıcı_gör(x):
    say=1
    print("-"*30)
    for i in x:
        print(str(say)+"-Kullanıcı Adı:",i)  #say int bir değer olduğundan dolayı + kullandık ve str kullandık.
        say+=1
    print("-"*30)
    input("Devam Etmek İçin Enter Tuşuna Basınız.")

def seç(x):
    print("-"*30)
    say=1
    kişi_seç=int(input("Kaç kişi seçilsin ?:"))
    rastgele_seç = random.sample(x,kişi_seç)

    for i in rastgele_seç:
        print(str(say)+"-Kullanıcı Adı:",i)
        say+=1
        print("Diğer kişi sistemden çekiliyor...")
        time.sleep(3)
    print("-"*30)
    input("Devam Etmek İçin Enter Tuşuna Basınız.")

def salla(x):
    print("-"*30)
    say=1
    random.shuffle(x)

    for i in x:
        print(str(say)+"-Kullanıcı Adı:",i)
        say+=1
    print("-"*30)
    input("Devam Etmek İçin Enter Tuşuna Basınız.")


while True:

    print("****ÇEKİLİŞ UYGULAMASINA HOŞGELDİNİZ****")
    seçim=int(input("1-Kullanıcı Ekle\n2-Kullanıcı Gör\n3-Kullanıcıları Karıştır\n4-Rastgele Seç\n5-Çıkış\n"))

    if seçim==1:
        kullanıcı_ekle(kullanıcılar)

    elif seçim==2:
        kullanıcı_gör(kullanıcılar)

    elif seçim==3:
        salla(kullanıcılar)

    elif seçim==4:
        print("Kişi seçme alanı hesaplanıyor...")
        time.sleep(2)   #2 saniye beklemeyi sağlar.
        seç(kullanıcılar)
    
    elif seçim==5:
        print("Sistemden Çıkılıyor...")
        time.sleep(2)
        break

    else:
        print("Lütfen uygun bir tercih yapınız")    