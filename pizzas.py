import csv
from datetime import datetime


class Pizza:
    def __init__(self,describe,price):
        self.describe=describe
        self.price=price


    def get_description(self):
        return self.describe

    def get_cost(self):
        return int(self.price)




# pizza alt sınıflarım.

class Klasik(Pizza):
    def __init__(self,describe="Klasik severler için",price=23):
        Pizza.__init__(self,describe,price)

class Margarita(Pizza):
    def __init__(self,describe="Mis gibi zeytinyağı ile hazırlanmış Margarita pizza",price=25):
        Pizza.__init__(self,describe,price)

class Turk(Pizza):
    def __init__(self,describe="Bol malzemeli Türk pizza",price=34):
        Pizza.__init__(self,describe,price)

class Sade(Pizza):
    def __init__(self,describe="Fazla malzeme sevmem diyenlere sade pizza",price=20):
        Pizza.__init__(self,describe,price)


# decorator sınıfım.

class Decorator:
    def __init__(self,describe,price):
        self.describe=describe
        self.price=price

    def get_sauce_describe(self):
        return self.describe
    def get_sauce_cost(self):
        return int(self.price)





# sos sınıflarım.

class Zeytin(Decorator):
    def __init__(self,describe="Zeytin sosu",price=3):
        Decorator.__init__(self,describe,price)

class Mantarlar(Decorator):
    def __init__(self,describe="Mantar malzemeli",price=3):
        Decorator.__init__(self,describe,price)

class KeçiPeyniri(Decorator):
    def __init__(self,describe="Keçi peyniri malzemeli",price=3):
        Decorator.__init__(self,describe,price)

class Et(Decorator):
    def __init__(self,describe="Et parçacıkları",price=3):
        Decorator.__init__(self,describe,price)


class Sogan(Decorator):
    def __init__(self,describe="Kuru soğanlar",price=3):
        Decorator.__init__(self,describe,price)

class Mısır(Decorator):
    def __init__(self,describe="Mısır tanecikleri",price=3):
        Decorator.__init__(self,describe,price)



def main(): # main sayfam.



   toplamFiyat = [] #toplam fiyat listesi
   menu = open("Menu.txt", "r", encoding="utf-8")  # menu sayfasını dosyadan okuma
   read = menu.read()

   print(read)  # menu sayfasının gösterimi

   pizza = input(" Lütfen bir pizza seçiniz...   ")  # pizza seçimi yapılır

   if (pizza == "1"):
      print(Klasik().get_description())
      print("fiyatı = ", Klasik().get_cost())
      toplamFiyat.append(Klasik().get_cost())

   elif (pizza == "2"):
       print(Margarita().get_description())
       print("fiyatı = ", Margarita().get_cost())
       toplamFiyat.append(Margarita().get_cost())

   elif (pizza == "3"):
       print(Turk().get_description())
       print("fiyatı = ", Turk().get_cost())
       toplamFiyat.append(Turk().get_cost())

   elif (pizza == "4"):
       print(Sade().get_description())
       print("fiyatı = ", Sade().get_cost())
       toplamFiyat.append(Sade().get_cost())

   else:
       print("hatalı seçim, lütfen tekrar seçiminizi yapınız ! Menü tekrar gösterilecek")
       toplamFiyat.clear()  #hatalı seçim olursa listedeki fiyatları sil
       main() #hatalı tercih olursa menüyü tekrar göster


   #sos seçim kısmı

   sos = input("Lütfen bir pizza sosu seçiniz...   ")  # sos seçimi yapılır

   if (sos == "11"):
       print(Zeytin().get_sauce_describe())
       print("fiyatı=", Zeytin().get_sauce_cost())
       toplamFiyat.append(Zeytin().get_sauce_cost())


   elif (sos == "12"):
       print(Mantarlar().get_sauce_describe())
       print("fiyatı=", Mantarlar().get_sauce_cost())
       toplamFiyat.append(Mantarlar().get_sauce_cost())


   elif (sos == "13"):
       print(KeçiPeyniri().get_sauce_describe())
       print("fiyatı=", KeçiPeyniri().get_sauce_cost())
       toplamFiyat.append(KeçiPeyniri().get_sauce_cost())

   elif (sos == "14"):
       print(Et().get_sauce_describe())
       print("fiyatı=", Et().get_sauce_cost())
       toplamFiyat.append(Et().get_sauce_cost())


   elif (sos == "15"):
       print(Sogan().get_sauce_describe())
       print("fiyatı=", Sogan().get_sauce_cost())
       toplamFiyat.append(Sogan().get_sauce_cost())


   elif (sos == "16"):
       print(Mısır().get_sauce_describe())
       print("fiyatı=", Mısır().get_sauce_cost())
       toplamFiyat.append(Mısır().get_sauce_cost())


   else:
       print("hatalı sos seçimi yaptınız , lütfen tekrar seçim yapınız")
       toplamFiyat.clear()  # hatalı seçim olursa listedeki fiyatları sil
       main() #hatalı tercih olursa menüyü tekrar göster


   if(sum(toplamFiyat)>0):

    # en fazla birinin doğru seçim yapılması durumunda listeye fiyat girilir ama en fazla birinin yanlış seçilmesi durumunda
    # else bloğundaki clear methodu, doğru girilen seçimden kalan fiyatı siler ve fiyat 0 olarak görünür.
    # Müşteriye ancak bütün seçimlerinin doğru olduğu durumdaki fiyat gösterilir bu if bloğunda

       print("Toplam tutar: ", sum(toplamFiyat),"$")  # toplam ücret gösterilir



   time = datetime.now().strftime("%Y-%m-%d %H:%M %p")


   data=[] # kullanıcıdan alınan veriler bu listeye alınır
   nickName = input(" Lütfen kullanıcı adınızı giriniz :  ")
   password = int(input("Lütfen kullanıcı kimliğinizi giriniz :    "))
   cardInfo = int(input("Lütfen kart bilgilerinizi giriniz :  "))
   cardPassword=int(input("Lütfen kart şifrenizi giriniz :  "))
   describe=f"{nickName} tarafından ({time}) tarihinde sipariş verilmiştir."


   data.append(nickName)
   data.append(password)
   data.append(cardInfo)
   data.append(cardPassword)
   data.append(describe)


   customerInfo = open("Orders_Database.csv",mode="a",encoding="utf-8") # database sayfamıza türkçe karakterler olarak bilgiler eklenir
   yaz = csv.writer(customerInfo)

   yaz.writerow(data) # database sayfamıza müşteri bilgileri yazılır

   print("İYİ GÜNLER DİLERİZ, AFİYET OLSUN...")





main()





