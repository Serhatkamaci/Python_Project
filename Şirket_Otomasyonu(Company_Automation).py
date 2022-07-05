import time
mesai = {}
def Menu():
    print(
        "-----------------------------------------\n          SİRKET OTOMASYONU          \n\n1 -> Ekleme\n2 -> Arama\n3 -> Silme\n4 -> Guncelleme\n5 -> Bilgileri Gosterme\n6 -> Maas Hesaplama\n----------------------------------------\n")
    islem = input("Lutfen yukarida verilenlere gore bir islem numarasi giriniz : ")
    if (islem == "1"):
        Ekle()
    if (islem == "2"):
        Arama()
    if (islem == "3"):
        Silme()
    if (islem == "4"):
        Guncelleme()
    if (islem == "5"):
        Bilgileri_Goster()
    if (islem == "6"):
        Maas_Hesaplama()


def Ekle():
    sirketteki_bolumler = ("Ticaridepartman", "Insankaynaklari", "Finans", "Idari")
    i_d = 1
    ad = input("\nKisinin adini giriniz : ")
    soyad = input("Kisinin soyadini giriniz : ")
    yas = input("Kisinin yasini giriniz : ")
    tel_no = input("Kisinin telefon numarasi : ")
    bolumu = input("Sirketteki konumunu giriniz : ")
    bolumu = bolumu.capitalize()

    if bolumu not in sirketteki_bolumler:
        print("\nSirketimizde '{}' adli bir bolum yoktur , lutfen kisiye ait uygun bolumu giriniz".format(bolumu))
        bolumu = input("Sirketteki konumu giriniz(Lutfen kelimeler arasinda bosluk birakmayiniz ) : ")
        bolumu = bolumu.capitalize()

    with open("calisanlar.txt", "r", encoding="utf-8") as dosya:
        calisanlar_listesi = dosya.readlines()

        if len(calisanlar_listesi) == 0:
            i_d = 1
        else:
            with open("calisanlar.txt", "r") as dosya:
                i_d = int(calisanlar_listesi[-1].split(")")[0]) + 1

    with open("calisanlar.txt", "a+") as dosya:
        dosya.write("{}){}-{}-{}-{}-{}\n".format(i_d, ad, soyad, yas, tel_no, bolumu))


def Silme():
    with open("calisanlar.txt", "r", encoding="utf-8") as dosya:
        calisanlar = dosya.readlines()
        print("\nSirketimizde yer alan calisanlarimiz\n")
        calisanlar2 = []
        for i in calisanlar:
            calisanlar2.append(" ".join(i[:-1].split("-")))
        for i in calisanlar2:
            print(i)

        while True:
            i_d2 = int(input(
                "\nLutfen cikarmak istediginiz kisinin id degerini giriniz (İd degerleri 1-{} arasindadir.): ".format(
                    len(calisanlar2))))

            if i_d2 > len(calisanlar2):
                print("{} id'li kisi sirkette bulunmamaktadir .".format(i_d2))
            else:
                print("\nSirketimizden cikarilan kisi")
                print("------------------------------------------------------")
                print(calisanlar2[i_d2 - 1])
                print("------------------------------------------------------\n")
                calisanlar.pop(i_d2 - 1)
                mesai[str(i_d2)] = 0
                break

    with open("calisanlar.txt", "w", encoding="utf-8") as dosya:
        dosya.writelines(calisanlar)

    with open("calisanlar.txt", "r", encoding="utf-8") as dosya2:
        calisanlar = dosya2.readlines()
        d = []
        s = 1
        for i in calisanlar:
            d.append(str(s) + ")" + " " + i.split(")")[1])
            s += 1

    with open("calisanlar.txt", "w", encoding="utf-8") as dosya2:
        dosya2.writelines(d)  # Liste kaydeder


def Arama():
    calisanlar2 = []
    with open("calisanlar.txt", "r", encoding="utf-8") as dosya:
        calisanlar = dosya.readlines()
    for i in calisanlar:
        calisanlar2.append(" ".join(i[:-1].split("-")))

    while True:
        i_d = int(input("Lutfen sorgulayacaginiz kisinin id degerini giriniz (Id deger 1-{} arasindadir.) : ".format(
            len(calisanlar2))))
        if i_d > len(calisanlar2):
            print("{} id'li kisi sirketimizde bulunmamaktadir.".format(i_d))
        else:
            print("\n{} id'li kisi asagida goruntuleniyor ...".format(i_d))
            time.sleep(1)
            print("-----------------------")
            print(calisanlar2[i_d - 1])
            print("-----------------------\n")
            break


def Guncelleme():
    with open("calisanlar.txt", "r", encoding="utf-8") as dosya2:
        calisanlar2 = dosya2.readlines()
        calisanlar2_kontrol = []
        while True:
            i_d = input(
                "Degistirmek istediginiz kisinin id'sini giriniz (Id'ler 1-{} arasindadir.)".format(len(calisanlar2)))
            if int(i_d) > len(calisanlar2):
                print("{} id'li kisi sirketimizde yer almamaktadir.".format(i_d))
            else:
                empty = ""
                for i in calisanlar2:
                    calisanlar2_kontrol.append(i.split(")"))
                for i in calisanlar2_kontrol:
                    if i[0] == i_d:
                        secim = input(
                            "\n1-) İsim Degistirme\n2-) Soyisim Degistirme\n3-) Yas Degistirme\n4-) Telefon Numarasi Degistirme\n5-) Sirket bolumunu degistirme\n\nLutfen yapacaginiz secimi giriniz : \n")
                        if secim == "1":
                            j = i[1].split("-")
                            yeni_isim = input("Lutfen bir isim giriniz : ")
                            j[0] = yeni_isim
                            empty = "{}-{}-{}-{}-{}".format(j[0], j[1], j[2], j[3], j[4])
                            i[1] = empty
                        if secim == "2":
                            j = i[1].split("-")
                            yeni_soyisim = input("Lutfen bir soyisim giriniz : ")
                            j[1] = yeni_soyisim
                            empty = "{}-{}-{}-{}-{}".format(j[0], j[1], j[2], j[3], j[4])
                            i[1] = empty

                        if secim == "3":
                            j = i[1].split("-")
                            yeni_yas = input("Lutfen bir yas giriniz : ")
                            j[2] = yeni_yas
                            empty = "{}-{}-{}-{}-{}".format(j[0], j[1], j[2], j[3], j[4])
                            i[1] = empty

                        if secim == "4":
                            j = i[1].split("-")
                            yeni_telno = input("Lutfen bir telefon numarasi giriniz : ")
                            j[3] = yeni_telno
                            empty = "{}-{}-{}-{}-{}".format(j[0], j[1], j[2], j[3], j[4])
                            i[1] = empty

                        if secim == "5":
                            j = i[1].split("-")
                            yeni_bolum = input("Lutfen bir bolum giriniz : ")
                            j[4] = yeni_bolum
                            empty = "{}-{}-{}-{}-{}\n".format(j[0], j[1], j[2], j[3], j[4])
                            i[1] = empty

                        b = i_d + ")" + empty
                        calisanlar2[int(i_d) - 1] = b
                break

        with open("calisanlar.txt", "w", encoding="utf-8") as dosya3:
            dosya3.writelines(calisanlar2)


def Bilgileri_Goster():
    d = {}
    i_d = 1
    with open("calisanlar.txt", "r", encoding="utf-8") as dosya:
        calisanlar = dosya.readlines()

        for i in calisanlar:
            d[i_d] = [i.split(")")[1].split("-")[0].lstrip()] + i.split(")")[1].split("-")[1:]
            i_d += 1
        with open("bilgilerigoster.txt", "w", encoding="utf-8") as dosya2:
            t = " "
            for i in d:
                for j in d[i]:
                    k = j + " "
                    t = t + k
                dosya2.write(t)
                t = ""
            """
            Burada "bilgileri goster" dosyasina degerler yazildi .

            """
    for i in d:
        k = d[i]
        print("\n\n----------------------\nAdi : {}\nSoyadi : {}\nYasi : {}\nTelefon Numarasi : {}\nSirketteki Bolumu: {}\n----------------------\n\n".format(k[0], k[1], k[2], k[3], k[4]))


def Maas_Hesaplama():
    def Mesai_Hesaplama():
        print("""

        Saatlik Mesai Ucreti -----> Sirketteki bolum durumuna gore degisir.
                                    Gunluk maasinin 2 kati ucret olarak saatine yansir .

        """)
        print("\n\n")

        with open("calisanlar.txt", "r", encoding="utf-8") as dosya:
            calisanlar = dosya.readlines()
        max = len(calisanlar)
        print("Eger bir id degeri iki kere girilirse onun mesai saati girilen id tekrari kadar artar .")
        for i in range(max):
            while True:
                j = input("Lutfen bir id giriniz(Id'ler 1-{} arasindadir) : ".format(max))
                if int(j)>max:
                    print("{} id'li bir kisi sirketimizde yoktur .Lutfen tekrardan bir id degeri giriniz .(Id'ler 1-{} arasindadir)".format(j,max))
                else:
                    if j not in mesai:
                        mesai[j] = 1
                        break
                    else:
                        mesai[j] += 1
                        break
        with open("mesai.txt", "a") as dosya:
            for i in calisanlar:
                id_degeri = i.split(")")[0]
                if id_degeri in mesai:
                    mesai_kalanlar = i.split(")")[1].split("-")[0] + " " + i.split(")")[1].split("-")[
                        1] + " " + "Mesaiye Kaldigi saat : " + str(mesai[id_degeri])
                    dosya.write(mesai_kalanlar + "\n")
                else:
                    print("{} id'li kisi mesaiye kalmiyor .".format(i.split(")")[0]))

    print(""""
    ----------------------Maas Heasbi İcin Saat Ucretleri----------------------
    1 -> Ticari Departman : 20
    2 -> İnsan Kaynaklari : 40
    3 -> Finans : 60
    4 -> İdari : 80
    """)

    with open("calisanlar.txt", "r", encoding="utf-8") as dosya:
        calisanlar = dosya.readlines()
        uzunluk = len(calisanlar)
        while True:
            i_d = input("Lutfen maasini sorgulayacaginiz kisinin id degerini giriniz (Id degeri 1-{} arasindadir.) : ".format(uzunluk))
            if int(i_d)>uzunluk:
                print("{} id'li bir kisi sirketimizde yoktur .Lutfen tekrardan bir id degeri giriniz .(Id'ler 1-{} arasindadir)".format(i_d,uzunluk))
            else:
                break
        secim = input("Aylik maas hesabi icin '1'i Yillik maas hesabi icin '2'yi tuslayiniz : ")

        if secim == "1":
            d = []
            for i in calisanlar:
                if i.split(")")[0] == i_d:
                    d.append(i.split(")")[1][:-1].split("-"))
            for i in d:
                if (i[-1] == "Ticaridepartman"):
                    maas = 20 * 30
                if (i[-1] == "Insankaynaklari"):
                    maas = 40 * 30
                if (i[-1] == "Finans"):
                    maas = 60 * 30
                if (i[-1] == "Idari"):
                    maas = 80 * 30
            mesai_secimi = input("Mesai'ye kalmak isterseniz 'E' harfini kalmak istemezseniz 'H' harfini tuslayiniz : ")
            if mesai_secimi == "E":
                Mesai_Hesaplama()
                print(mesai)
                if i in d:
                    if (i[-1] == "Ticaridepartman" and i_d in mesai):
                        maas = maas + (40 * mesai[i_d])
                    if (i[-1] == "Insankaynaklari" and i_d in mesai):
                        maas = maas + (80 * mesai[i_d])
                    if (i[-1] == "Finans" and i_d in mesai):
                        maas = maas + (120 * mesai[i_d])
                    if (i[-1] == "Idari" and i_d in mesai):
                        maas = maas + (160 * mesai[i_d])
                print("\n{} id'li kisinin mesai dahil aylik ucreti = {} TL'dir.\n".format(i_d, maas))

            if mesai_secimi == "H":
                print("\n{} id'li kisinin mesaisiz aylik ucreti = {} TL'dir.\n".format(i_d, maas))

        if secim == "2":
            s = []
            for i in calisanlar:
                if i.split(")")[0] == i_d:
                    s.append(i.split(")")[1][:-1].split("-"))
            for i in s:
                if (i[-1] == "Ticaridepartman"):
                    maas = 20 * 365
                if (i[-1] == "Insankaynaklari"):
                    maas = 40 * 365
                if (i[-1] == "Finans"):
                    maas = 60 * 365
                if (i[-1] == "İdari"):
                    maas = 80 * 365
            print("\n{} id'li kisinin mesaisiz yillik ucreti = {} TL'dir.\n".format(i_d, maas))

        for i in calisanlar:
            if i.split(")")[0] == i_d:
                maasi = i.split(")")[1].split("-")[0] + " " + i.split(")")[1].split("-")[1] + " " + "Maasi : " + str(
                    maas)
        with open("maaslar.txt", "a+", encoding="utf-8") as dosya2:
            dosya2.write(maasi + "\n")


print(
    "\n\n\n*********************************\n\n1 -> Programi Baslatma\n2 -> Programdan Cikis\n\n*********************************\n\n")

print("""
------------------------Sirketimizde Yer Alan Bolumler------------------------
1 -> Ticari Departman
2 -> İnsan Kaynaklari
3 -> Finans
4 -> İdari 
""")
while True:
    k = input("Lutfen yapmak istediginiz secimi yukarida verilen bilgilere gore giriniz : ")
    if (k == "1"):
        Menu()
        print("\n\nDevam etmek icin 1'i Cikis icin 0'i tuslayiniz\n\n")
    if (k == "0"):
        print("\nUygulamadan Cikis Yapiliyor")
        time.sleep(2)
        print("Uygulamamizi kullandiginiz icin tesekkurler")
        break
