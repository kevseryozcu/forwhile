print("""
************************
atm makinesine hosgeldiniz

1. işlem bakiye sorgulama

2. işlem para yatırma işlemi

3. işlem para çekme işlemi

programdan çıkmak için q tuşuna basınız
************************
""")

bakiye = 1000
while True:
    islem = input("işlemi seçiniz: ")
    if islem == "q":
        print("yine bekleriz")
        break
    elif islem == "1":
        print("bakiyeniz: {} tl dir".format(bakiye))

    elif islem == "2":
        miktar = int(input("yatırmak istediğiniz miktarı giriniz"))
        bakiye += miktar

    elif islem == "3":
        miktar = int(input("çekmek istediğiniz miktarı giriniz"))
        if bakiye - miktar < 0:
            print("bakiyeniz yetersiz")
            continue
        bakiye -= miktar
    else:
        print("geçersiz işlem")
