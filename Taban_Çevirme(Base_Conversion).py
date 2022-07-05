print("""
-----------------------------------------------------

Taban Cevirme Programi

1 --> 2'lik tabandaki sayilari 10'luk tabana cevirme
2 --> 10'luk tabandaki sayilari 2'lik tabana cevirme
3 --> Programdan Cikis

-----------------------------------------------------
""")
while True:
    secim = input("Lutfen istediginiz secimi giriniz : ")
    if(secim=="1"):
        print("2'lik taban programina hosgeldiniz ...")
        sayi = input("2'lik tabandaki sayiyi giriniz : ")
        while True:
            if("2" in sayi or "3" in sayi or "4" in sayi or "5" in sayi or "6" in sayi or  "7" in sayi or "8" in sayi or "9" in sayi=="True"):
                sayi = input("Lutfen 2'lik tabana uygun bir sayi degeri giriniz : ")
            else:
                sayi = int(sayi)
                toplam = 0
                k = 0
                while (sayi > 0):
                    a = sayi % 10
                    if (a == 1):
                        toplam += (2 ** k) * a
                        k += 1
                    elif (a == 0):
                        toplam += (2 ** k) * a
                        k += 1
                    b = sayi // 10
                    b, sayi = sayi, b
                print("Sayinin onluk tabandaki degeri : ", toplam)
                break




    elif(secim=="2"):
        print("Onluk taban programina hosgeldiniz ...")
        sayi = int(input("Onluk tabandaki sayiyi giriniz : "))
        x=""
        while(sayi>0):
            a=sayi%2
            x+=str(a)
            b=sayi//2
            b,sayi=sayi,b
        print("Sayinin 2'lik tabandaki degeri : ",x[::-1])
    elif(secim=="3"):
        print("Programdan Cikis Yapiliyor ...")
        break

