print("""
************************
kullanıcı giriş programı 
************************
""")
syskullanici = "kevser"
sysparola = "123456"
giris = 3

while True:
    kullanici = input("kullanıcı adınızı giriniz: ")
    parola = input("parolayı giriniz: ")
    if kullanici != syskullanici and parola == sysparola:
        print("kullanıcı adı hatalı")
        giris -= 1
    elif kullanici == syskullanici and parola != sysparola:
        print("parola hatalı")
        giris -= 1
    elif kullanici != syskullanici and parola != sysparola:
        print("kullanıcı adı ve parola hatalı")
        giris -= 1
    else:
        print("başarıyla giriş yapıldı ")
        break
    if giris == 0:
        print("giriş hakkınız kalmadı")
