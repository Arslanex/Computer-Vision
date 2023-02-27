<h3 align="center"> Please Chose a Language </h3>

<button>asd</button>

***

# Evrişimsel Sinir Ağlarının Temelleri

Herkese merhaba,
Eğer ileri seviye bilgisayar görüsü ile uğraşmak istiyorsanız yolunuz mutlaka bir yerede evrişimsel sinir ağları yani CNN'ler ile karşılaşacaktır. Günümüzde bu CNN teknolojisini
kullanan bir çok yazılım var. Yolo'nun farklı versionları ve RCNN yazılımıları örnek olabilir. Her ne kadar bunları belirli bir düzeyde kullanmak için CNN'ler ile ilgili herhangi bir bilgiye sahip olmanız gerekmese bile bu nöral ağları efektif kullanmak için CNN yapısının arkasındaki dönen olaylara hakim olmanız gerekmektedir.

Bu repmda OpenCV kütüphanesi yardımı ile sıfırdan bir evrişimsel sinir ağı (CNN) örneği oluşturacağım bu süreçte nöral ağlar ile ilgli bir çok terimi ve arkada gerçekleşen matematiksel işlemleri en temel düzeyde gözlemleyebileceksiniz. Bu notlardan en üst düzey verimi alabilmek için:
- Python programlama dilini bilmek
- OpenCV kütüphanesinin temellerni bilmek
- Matrisler ile temel matematiksel işlemlere hakim olmak

gerekmektedir. Başlamadan önce nöral ağlar ile ilgili yazdığım yazıyı okuyarak nöral ağların teorisi ve terimler ile ilgili daha fazla bilgi öğrenebilirsiniz. Umarım notlarım sizler için yararlı olur. Sizlere iyi çalışmalar.

## Dosya Yapısı

```
.
├── Notebooks (EN)                                      # İngilizce Notlar
├── Notebooks (TR)                                      # Türkçe Notlar
│   ├── 1. Basit Resim sınıflandırıcı.ipynb             # Eğitim notu
│   ├── 2. Otomatik Resim Sınıflandırıcı.ipynb          # Eğitim notu
│   ├── 3. Basit Bir CNN Oluşturalım.ipynb              # Eğitim notu
│   ├── 3.1 Nöral Ağımızı Deneyelim.py                  # Birleştirilmiş python dosyası
│   ├── 4. Ağırlıkları Ayarlayalım.ipynb                # Eğitim Notu
│   ├── 5. Etiketler ve Verisetleri.ipynb               # Eğitim nout
│   ├── (yüklenmedi)
│   ├── (yüklenmedi)
│   └── (yüklenmedi)
├── dataset                                              # Kullanılacak eğitim ve test görselleri
└── README.md

```

## Kazanımlar
### 1. Basit Resim sınıflandırıcı
Bilgisayarlarlar için resimlerin nasıl göründüğünü, resimler üzerinde nasıl işlem yapabildiklerini ve resimleri nasıl sınıflandırdığını anlamaya çalışacağız. Bunun için de Python programlama dilini kullanarak basit bir sınıflandırıcı oluşturacağız.

### 2. Otomatik Resim Sınıflandırıcı
İlk bölümde oluşturduğumuz sınıflandırcı kodunun üzerine eklemeler yaparak programın sınıflandırma için uygun filtreyi kendi kendine oluşturmasını sağlayacağız.

### 3. Basit Bir CNN Oluşturalım
Basit bir CNN oluşturacağız. Bu sırada konvolüsyon, aktivasyon fonksiyonu, ağırlık (weights) ve eşik değer kavramlarına bakacağız. 

### 3.1 Nöral Ağımızı Deneyelim
Bir önceki bölümde kullanılan  kodların derlenmiş ve fonksiyon haline getirilmiş halidir. Burada bulunan CNN henüz doğru tahmin yapamamaktadır.

### 4. Ağırlıkları Ayarlayalım
Ağırlıkların yeniden ayarlanmasının arkasındaki matematiğe bakacak ve kendi ağırlıklarımızı dikey çizgi içeren resime göre yeniden ayarlayacağız.

### 5. Etiketler ve Verisetleri
Geçtiğimiz bölümde işlenen ağırlıkları yeniden ayarlama işlemini her iki resime göre ayarlanacak şekilde güncelleyecek ve bir eğitim döngüsü oluşturacağız. Böylece istediğimiz tur sayısı kadar eğitim işlemi gerçkeleştirebileceğiz.

***
<h3 align="center"> Enes ARSLAN </h3>
<p align="center">
<a href="https://www.instagram.com/_enes.arslan_/?next=%2F">
<img src="https://img.shields.io/badge/Instagram-000000?style=for-the-badge&logo=instagram&logoColor=white"/>
<a href="https://www.linkedin.com/in/enes-arslan-/">
<img src="https://img.shields.io/badge/LinkedIn-000000?style=for-the-badge&logo=linkedin&logoColor=white"/>
<a href="https://github.com/Arslanex">
<img src="https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white"/ >
</p>
