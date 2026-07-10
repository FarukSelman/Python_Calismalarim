#Hata yakalamadır.
import time

try :
    sayı=int(input("Sayı 1: "))
    sayı1=int(input("Sayı 2: "))

    toplam=sayı+sayı1
    print(toplam)


except (ZeroDivisionError,ValueError):
    print("Hata")

finally :
    sayac = 5
    for i in range(5):
        time.sleep(1)
        print("Geri sayım :",sayac)
        sayac-=1
        if sayac==0:
            print("İşlem tamamlandı")

        
"""
except  ZeroDivisionError:
    print("Bir sayı sıfıra bölünemez.")

except ValueError:
    print("Lütfen sayısal veri giriniz.")
""" 



