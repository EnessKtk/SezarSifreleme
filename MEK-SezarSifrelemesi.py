def sifreli(metin, anahtar):
    sifreliMetin= ""
    for i in metin:
        sifreliMetin = sifreliMetin + chr(ord(i) + anahtar)
    print(str("Şifreli Metin: "+ sifreliMetin))
def sifresiz(metin, anahtar):
    sifresizMetin = ""
    for i in metin:
        sifresizMetin = sifresizMetin + chr(ord(i) - anahtar)
    print(str("Şifresiz Metin: "+ sifresizMetin))
def kkuvvetDeneme(metin):
    sifresizMetin = ""
    anahtar = 1
    while anahtar < 33:
        for i in metin:
            sifresizMetin = sifresizMetin + chr(ord(i) - anahtar)
        print("Anahtar/Key/Ofset: "+str(anahtar) + "," " Şifresiz Metin= ",sifresizMetin)
        anahtar += 1
        sifresizMetin = ""
print("""
[1] Metni Şifrele
[2] Anahtarlı Şifreli Metni Bul
[3] Anahtarsız Şifreli Metni Bul
""")
secenek = int(input("Yukarıdaki Seçeneklerden Hangisi (1-2-3):"))
if secenek == 1:
    Metin = input("Şifrelenecek Metin: ")
    Anahtar = int(input("Anahtar/Key/Ofset Değeri: "))
    sifreli(Metin, Anahtar)
elif secenek == 2:
    Metin = input("Şifresi Bulunacak Metin: ")
    Anahtar = int(input("Anahtar/Key/Ofset Değeri: "))
    sifresiz(Metin, Anahtar)
elif secenek == 3:
    Metin = input("Şifresi Bulunacak Metin: ")
    kkuvvetDeneme(Metin)