import subprocess as sp

"""
subprocess.call("notepad.exe")  #direk not defterini açar . calc yazarsak eğer hesap makinesini açar
"""


psw="123456"
kullanıcı_sifre=input("Lütfen Şifrenizi Giriniz: ")
if kullanıcı_sifre==psw:

    while True:
        print("***UYGULAMA AÇMA EKRANINA HOŞGELDİNİZ***")

        seçim_yap=input("1-Notepad\n2-Microsoft Edge\n3-Google\n4-Hesap Makinesi\n5-Çıkış\n")

        if seçim_yap=="1":
            sp.call("notepad.exe")
            input("Devam edilsin mi ?")

        elif seçim_yap=="2":
            sp.call("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")  
            input("Devam edilsin mi ?")

        elif seçim_yap=="3":
            sp.call("C:\Program Files\Google\Chrome\Application\chrome.exe") 
            input("Devam edilsin mi ?")
        
        elif seçim_yap=="4":
            sp.call("calc.exe")
            input("Devam edilsin mi ?")

        elif seçim_yap=="5":
            break

else:
    print("Hatalı Şifre")