from pytube import YouTube

def bilgileri_goster():
    url = YouTube(input("Lütfen Bilgilerini Görmek İstediğiniz Linki Yapıştırınız: "))
    
    try:
        son_dakika = url.length / 60
    except TypeError:
        son_dakika = "Bilinmiyor"

    print("-" * 45)
    print("Videonun Başlığı:", url.title)
    print("Videonun Sahibi:", url.author)
    print("Videonun Küçük Resmi:", url.thumbnail_url)
    print("İzlenme Sayısı:", url.views)
    print("Videonun Uzunluğu:", son_dakika, "dakika")
    print("-" * 45)


def video_indir():
    url = YouTube(input("Lütfen İndirilecek Video Linkini Yapıştırınız: "))

    try:
        son_dakika = url.length / 60
    except TypeError:
        son_dakika = "Bilinmiyor"

    indirme_baglantisi = url.streams.filter(progressive=True).first()
    
    if indirme_baglantisi:
        indirme_baglantisi.download()
        print("Video başarıyla indirildi!")
    else:
        print("İndirilecek video bulunamadı!")

    print("-" * 45)
    print("Videonun Başlığı:", url.title)
    print("Videonun Sahibi:", url.author)
    print("İzlenme Sayısı:", url.views)
    print("Videonun Uzunluğu:", son_dakika, "dakika")
    print("-" * 45)


def ses_indir():
    url = YouTube(input("Lütfen İndirilecek Ses Linkini Yapıştırınız: "))

    try:
        son_dakika = url.length / 60
    except TypeError:
        son_dakika = "Bilinmiyor"

    indirme_baglantisi = url.streams.filter(only_audio=True).first()
    
    if indirme_baglantisi:
        indirme_baglantisi.download()
        print("Ses dosyası başarıyla indirildi!")
    else:
        print("İndirilecek ses dosyası bulunamadı!")

    print("-" * 45)
    print("Ses Başlığı:", url.title)
    print("Ses Sahibi:", url.author)
    print("İzlenme Sayısı:", url.views)
    print("Videonun Uzunluğu:", son_dakika, "dakika")
    print("-" * 45)


bilgileri_goster()
