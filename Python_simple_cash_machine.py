kartsifre = 1234
bakiye = 500
login = False



while True:
    if login == False:
        sifre = int(input(" Şifrenizi giriniz. "))         
    if sifre == kartsifre:  
        login = True
        print("""
1. para çekme
2. paray yatırma
3. bakiye sorgulama 
4. kart iade
              """)
        secim = int(input(" işleminizi seçiniz? "))
    if secim == 1:
        miktar = int(input(" çekmek istediğiniz para miktarı? şuan ki miktar {} ".format(bakiye)))
        if bakiye < miktar:
            print(" yeterli bakiyeniz bulunmamaktadır. ")
            print("Bakiyeniz {}tl".format(bakiye))
            continue
        bakiye -= miktar
#para çekmek için 1
    elif secim == 2:
        miktar = int(input(" yatırmak istediğiniz para miktarı? "))
        bakiye += miktar
        print("işleminiz başarıyla gerçekleşmiştir :D ana menüye yönlendiriliyorsunuz.")
        print("Bakiyeniz {} tl".format(bakiye))
#para yatırmak için 2
    elif secim == 3:
        print("Bakiyeniz {}tl".format(bakiye))
#var olan bakiyeyi sorgulamak için 3
    elif secim == 4:
        print("Güle Güle")
        break
#çıkış yapmak için 4
    else:
        print("1-4 aralığında bir seçim yapınız")
#istediğim bütün işlemleri yapabiliyorum 