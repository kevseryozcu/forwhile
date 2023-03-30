print("""
************************
faktoriyel bulma programı

çıkış için q tuşuna basınız
************************
""")
while True:

    sayi = input("bir sayı giriniz: ")
    if sayi == "q":
        print("program sonlandırıldı")
        break
    else:
        sayi = int(sayi)
        faktoriyel = 1

        for i in range(2, sayi+1):
            faktoriyel *= i
        print("faktoriyeliniz ", faktoriyel)
