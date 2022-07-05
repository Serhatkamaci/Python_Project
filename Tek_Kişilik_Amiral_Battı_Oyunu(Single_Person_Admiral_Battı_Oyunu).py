print("""
----------------------------------------------

************ AMİRAL BATTİ OYUNU ************

            Secim Degeri İcin
            
-------------------------------------------------------------------------
Soldaki degerler ile sagdaki degerler arasinda bir secim yapabilirisiniz
-------------------------------------------------------------------------

1-) gizli   --->  Gizli Mod
2-) acik    --->  Acik Mod
3-) oyun    --->  Oyunu Oyna
4-) temizle --->  Oyun Alanlarini Temizleme
5-) cikis   --->  Oyundan Cikis

----------------------------------------------
""")
import random
import time
satir=int(input("Lutfen boyut degerini giriniz : "))
sutun=satir
gemi=[1,2,3,4]
koordinat_kontrol=list()
yatay_mi_dikey_mi=["yatay","dikey"]
matris = list()
matris2 = list()

while True:
    secim=input("Lutfen bir secim degeri giriniz : ")
    if(secim=="gizli"):
        print("----------------Gizli Mod Alani----------------\n")
        sutun_numaralari=list()
        for i in range(0, satir):
            sutun_numaralari.append(str(i))
        b = " ".join(sutun_numaralari)
        print("\t\t\t  ", b)
        for i in range(satir):
            matris.append(["?"] * sutun)
        k=0
        for i in matris:
            print("\t\t\t",k,end=" ")
            for j in i:
                print(j, end=" ")
            print()
            k+=1
        k=0
        print("\n\n")


    elif(secim=="acik"):
        print("----------------Acik Mod Alani----------------\n")
        sutun_numaralari2=list()
        for i in range(0, satir):
            sutun_numaralari2.append(str(i))
        b = " ".join(sutun_numaralari2)
        print("\t\t\t  ", b)
        for i in range(satir):
            matris2.append(["?"] * sutun)
        k=0
        for i in matris2:
            print("\t\t\t",k, end=" ")
            for j in i:
                print(j, end=" ")
            print()
            k += 1
        print("\n\n")

        def gemi_yerlestir(gemi_satir, gemi_sutun, yatay_dikey, boyut):
            kontrol = None
            for i in range(1):
                if (yatay_dikey == "yatay"):
                    if (boyut + gemi_sutun > 9):
                        print("Bu gemi sutun alaninin disina cikacagi icin yerlestirilemez ...")
                        gemi_satir = random.randint(0, 9)
                        gemi_sutun = random.randint(0, 9)
                        print("Yeni Satir ve Sutun koordinatlari : ({},{})".format(gemi_satir, gemi_sutun))
                        yatay_dikey=random.choice(yatay_mi_dikey_mi)
                        print("Yeni gemi yerlestirme seklimiz {}".format(yatay_dikey))
                        gemi_yerlestir(gemi_satir,gemi_sutun,yatay_dikey,boyut)


                    else:
                        for l in range(boyut):
                            sembol = matris2[gemi_satir ][gemi_sutun + l]
                            if (sembol == "O"):
                                kontrol = 1
                                break
                        if (kontrol == 1):
                            print("Bulundugunuz konum dolu oldugu icin buraya gemi yerlestirilemez")
                            gemi_satir = random.randint(0, 9)
                            gemi_sutun = random.randint(0, 9)
                            print("Yeni Satir ve Sutun koordinatlari : ({},{})".format(gemi_satir, gemi_sutun))
                            yatay_dikey = random.choice(yatay_mi_dikey_mi)
                            print("Yeni gemi yerlestirme seklimiz {}".format(yatay_dikey))
                            gemi_yerlestir(gemi_satir, gemi_sutun, yatay_dikey, boyut)

                        else:
                            for z in range(boyut):
                                matris2[gemi_satir][gemi_sutun + z] = "O"

                else:
                    if (boyut + gemi_satir > 9):
                        print("Bu gemi satir alaninin disina cikacagi icin yerlestirilemez ...")
                        gemi_satir = random.randint(0, 9)
                        gemi_sutun = random.randint(0, 9)
                        print("Yeni Satir ve Sutun koordinatlari : ({},{})".format(gemi_satir, gemi_sutun))
                        yatay_dikey = random.choice(yatay_mi_dikey_mi)
                        print("Yeni gemi yerlestirme seklimiz {}".format(yatay_dikey))
                        gemi_yerlestir(gemi_satir, gemi_sutun, yatay_dikey, boyut)

                    else:
                        for p in range(boyut):
                            sembol = matris2[gemi_satir + p][gemi_sutun ]
                            if (sembol == "O"):
                                kontrol = 1
                                break
                        if (kontrol == 1):
                            print("Bulundugunuz konum dolu oldugu icin buraya gemi yerlestirilemez")
                            gemi_satir = random.randint(0, 9)
                            gemi_sutun = random.randint(0, 9)
                            print("Yeni Satir ve Sutun koordinatlari : ({},{})".format(gemi_satir, gemi_sutun))
                            yatay_dikey = random.choice(yatay_mi_dikey_mi)
                            print("Yeni gemi yerlestirme seklimiz = {}".format(yatay_dikey))
                            gemi_yerlestir(gemi_satir, gemi_sutun, yatay_dikey, boyut)
                        else:
                            for e in range(boyut):
                                matris2[gemi_satir + e ][gemi_sutun] = "O"

        def gemi_koordinatlarini_al(gemi):
            for i in gemi:
                boyut = i
                print("Gemi boyutu : ", boyut)
                gemi_satir = random.randint(0, 9)
                gemi_sutun = random.randint(0, 9)
                print("{}.Satir ve sutun  koordinati= ({},{})".format(i, gemi_satir, gemi_sutun))
                yatay_dikey = random.choice(yatay_mi_dikey_mi)
                print("Gemi Yerlestirilme Sekli : ",yatay_dikey)
                gemi_yerlestir(gemi_satir, gemi_sutun, yatay_dikey, boyut)

        gemi_koordinatlarini_al(gemi)
        print("\n\n")
        for i in matris2:
            for j in i:
                print(j, end=" ")
            print()

    elif(secim=="oyun"):
        tahmin_hakki = (satir**2)//3
        atis=0
        t=0
        kontrol2=0
        while True:
            if(t==0):
                oyunucu_satir = int(input("Lutfen bir satir numarasi giriniz : "))
                oyuncu_sutun = int(input("Lutfen bir sutun numarasi giriniz : "))
                x=str(oyunucu_satir) + str(oyuncu_sutun)
                atis+=1
                koordinat_kontrol.append(x)
                t+=1

            else:
                oyunucu_satir = int(input("Lutfen bir satir numarasi giriniz : "))
                oyuncu_sutun = int(input("Lutfen bir sutun numarasi giriniz : "))
                atis+=1
                y = str(oyunucu_satir) + str(oyuncu_sutun)
                if((y in koordinat_kontrol)):
                    print("Ayni koordinatlari girdiniz ....")
                    print("Lutfen baska bir koordinat noktasi seciniz ....")
                else:
                    koordinat_kontrol.append(y)


            if (matris2[oyunucu_satir][oyuncu_sutun] == "O"):
                print("Tebrikler bir gemi vurdunuz ...")
                matris2[oyunucu_satir][oyuncu_sutun] = "x"
                kontrol2+=1
                print("Kalan tahmin hakkiniz : ", tahmin_hakki)
                tahmin_hakki -= 1
            else:
                print("Maalesef isabet edemediniz ...")
                matris2[oyunucu_satir][oyuncu_sutun] = "*"
                print("Kalan tahmin hakkiniz : ", tahmin_hakki)
                tahmin_hakki -= 1
            if (tahmin_hakki == 0):
                print("Maalesef tahmin hakkiniz bitti ...")
                break
            if(kontrol2==10):
                print("Tebrikler tum gemileri vurdunuz , oyun sonlaniyor ...")
                time.sleep(2)
                print("Oyun sonlandi .")
                print("Puan Hesaplaniyor ...")
                time.sleep(2)
                puan=tahmin_hakki-atis
                print("Toplam Puaniniz : ",puan)
                break

            for i in matris2:
                for j in i:
                    print(j, end=" ")
                print()
            print("\n\n")
        print("Yaptiginiz toplam atis sayisi : ",atis)
    elif(secim=="temizle"):
        del(matris)
        matris = list()
        print("Acik Mod Alani Temizlendi ...")
        del(matris2)
        matris2 = list()
        print("Gizli Mod Alani Temizlendi ...")
        satir = int(input("Lutfen boyut degerini giriniz : "))
        sutun = satir
        gemi = [1, 2, 3, 4]
        koordinat_kontrol = list()
        yatay_mi_dikey_mi = ["yatay", "dikey"]
        matris = list()
        matris2 = list()

    elif(secim=="cikis"):
        print("Amiral Battı Oyunundan Cikis Yapiliyor ...")
        time.sleep(2)
        print("Cikis Yapildi .")
        break
