def faktoriyel(sayi):
    faktoriyel = 1
    if sayi == 1 or sayi == 0:
        print("faktoriyel: ", faktoriyel)
    else:
        while sayi >= 1:
            faktoriyel *= sayi
            sayi -= 1
        print("faktoriyel: ", faktoriyel)


faktoriyel(5)
