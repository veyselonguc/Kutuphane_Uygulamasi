# 📚 Kütüphane Uygulaması
Python ile oluşturulmuş basit bir kütüphane uygulamasıdır.
Uygulama kitap ekleme, listeleme ve silme fonksiyonalitelerini terminal/komut satırı üzerinden sunmaktadır.

## 🔹 Özellikler
✅ Kitap ekleme

✅ Kitapları listeleme

✅ Kitap silme

✅ Metin dosyasında kalıcı veri saklama

✅ Menü tabanlı, terminal üzerinden kullanım

## 🔹 Dosya Yapısı
```bash
.
├── books.txt
├── kutuphane.py
├── README.md
```
-kutuphane.py: Ana Python script dosyasında kütüphane fonksiyonaliteleri yer alır.

-books.txt: Eklenen kitaplar bu metin dosasında kalıcı olarak saklanır.

## 🔹 Kurulum ve Kullanım
1️⃣ Python'un bilgisayarınıza kurulu olduğuna emin olun (Python 3+).
```bash
.
├── books.txt
├── kutuphane.py
├── README.md
```
2️⃣ Proje klasörünü bilgisayarınıza indirin ya da kopyalayın.
```bash
.
├── books.txt
├── kutuphane.py
├── README.md
```
3️⃣ Uygulamayı terminal/komut satırı içinde çalıştırın:
```bash
python kutuphane.py
```
4️⃣ Açılan menüde:
1: Kitapları Listele

2: Kitap Ekle

3: Kitap Sil

Q: Uygulamadan çık

## 🔹 Örnek
```bash
***************Kütüphane Uygulamasina Hosgeldiniz***************

-------MENU-------
1) Kitaplari Listeleme
2) Kitap Ekleme
3) Kitap Silme
Q) Cikis Yapma
```

## 🔹 Açıklamalar

AddBooks: books.txt içinde yeni satır oluşturur.

ListBooks: books.txt içinde kayıtlı olanları ekrana bastırır.

RemoveBooks: İstendiği zaman belirli kitapları books.txt içinde arayıp siler.
