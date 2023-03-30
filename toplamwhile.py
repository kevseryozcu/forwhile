toplam = 0
while True:
    sayi = input("sayi giriniz: ")
    if sayi == "q":
        break
    sayi = int(sayi)
    toplam += sayi
print("girilen sayıların toplamı: ", toplam)
