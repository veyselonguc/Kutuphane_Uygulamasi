import os # Terminal ekranını temizlemek için kod içerisinde kullanıldı.
import time # Gerekli bekletmeleri yapmak için kod içerisinde kullanıldı.
class Library():

    def __init__(self):
        # Dosyayı açma işlemi yapıyoruz.
        self.file = open("books.txt", "a+") 

    def __del__(self):
        # Dosyayı kapatma işlemi yapıyoruz.
        self.file.close()

    def AddBooks(self):
        # Kullanıcıdan kitap bilgilerini input fonksiyonu ile istiyoruz.
        kitap = [input("<> Kitap Adini Giriniz: "),input("<> Kitap Yazarini Giriniz: "),input("<> Kitap Sayfasini Giriniz: "),input("<> Kitap Yayinlanma Tarihi Giriniz: ")]
        # Dosyayı açma işleimini yapıp, kitap bilgilerini virgülle ayırarak yazıyoruz.
        with open("books.txt", "a+") as a:
            a.write(" , ".join(map(str,kitap)) + "\n")
        print("\nKitap Basariyla Eklendi.")
        time.sleep(1)

    def ListBooks(self):
        # Kitap Bilgilerini okutuyoruz.
        print("\n----------Kitap Listesi----------")
        with open("books.txt", "r") as a:
            kitaplar = a.read().splitlines()
        # Virgülle ayrılmış her veriyi dizinin bir elemanı olarak düşünüp sadece ilk iki indexi döndürüyoruz.
        for satir in kitaplar:
            KitapBilgisi = satir.split(" , ")
            print("kitap: " + KitapBilgisi[0] + "\t\tyazar: " + KitapBilgisi[1])
        
    def RemoveBooks(self):
        # Kitap Bilgilerini okutuyoruz.
        with open("books.txt","r") as a:
            kitaplar = a.read().splitlines()
        # Kullanıcıdan silmek istediği kitap adını istiyoruz.
        SatirSil = input("<> Silmek İstediginiz Kitabin Adi:\n")
        # Kitap bilgilerini virgüle göre ayırıp dizi haline getirip 0. indeksin kullanıcının girdiği değere eşit olup olmadığını inceliyoruz.
        for satir in kitaplar:
            KitapBilgisi = satir.split(" , ")
            if(KitapBilgisi[0]==SatirSil):
                kitaplar.remove(satir)
                print("\nKitap Basariyla Silindi.")
                time.sleep(1)
                break
        else:
            print("\n!!! Yanlis Bir İfade Girdiniz Tekrar Deneyiniz.")
            time.sleep(2)

        with open("books.txt", "w") as a:
            for satir in kitaplar:
                a.write(satir + "\n")

lib = Library() # Nesne tanımladık.

while True:
    os.system('cls')
    print("\n\n***************Kütüphane Uygulamasina Hosgeldiniz***************")
    print("\n\n-------MENU-------")
    # Kullanıcıdan yapmasını istediğimiz işlemin girdisini istiyoruz.
    print("1) Kitaplari Listeleme \n2) Kitap Ekleme \n3) Kitap Silme \nQ) Cikis Yapma\n------------------")
    KullaniciSecimi = input("\n<> Yapmak İstediginiz işlemi seciniz:\n(1,2,3,Q)\n")
    print("\nYonlendiriliyorsunuz...")
    time.sleep(1)
    # if-else metodunu kullanarak oluşturduğumuz fonksiyonları çalıştırıyoruz.
    if(KullaniciSecimi=="1"):
        os.system('cls')
        lib.ListBooks()
        girdi = input("\nDevam etmek icin entera basiniz:")
    elif(KullaniciSecimi=="2"):
        os.system('cls')
        lib.AddBooks()
    elif(KullaniciSecimi=="3"):
        os.system('cls')
        lib.RemoveBooks()
    elif(KullaniciSecimi.upper()=="Q"):
        os.system('cls')
        print("Cikis Yapiliyor...")
        time.sleep(1)
        break
    else:
        print("\n!!! Gecersiz bir ifade girdiniz.")
        time.sleep(1)