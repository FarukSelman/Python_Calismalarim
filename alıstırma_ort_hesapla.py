vize_notu=int(input("Vize Notunu Giriniz: "))
final_notu=int(input("Final  Notunuzu Giriniz: "))
ortalama_al=(vize_notu*0.4)+(final_notu*0.6)

if ortalama_al>=85:
    print("Tebrikler AA aldınız. Notunuz: ",ortalama_al)

elif ortalama_al>=65:
    print("Tebrikler BB aldınız. Notunuz: ",ortalama_al)

elif ortalama_al>=50:
    print("Tebrikler CC aldınız. Notunuz: ",ortalama_al)

else:
    print("Maalesef dersi geçemediniz.Ders tekrarı gerekiyor. Notunuz: ",ortalama_al)