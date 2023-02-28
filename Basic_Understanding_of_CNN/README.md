<div align="center">
 
[<kbd> <br> ENGLISH <br> </kbd>][KBD1]
[<kbd> <br> TÜRKÇE <br> </kbd>][KBD2]

</div>

<p align="center">
  <img src="https://user-images.githubusercontent.com/44752389/221812657-710eb794-e838-4eca-9cdd-378873e0bcc2.png" width="100%"/>
</p>
 
[KBD1]: #basic-understannding-of-convolutional-neural-networks
[KBD2]: #evrişimsel-sinir-ağlarının-temelleri

***
# Basic Understannding of Convolutional Neural Networks

Hello everyone,
If you want to deal with advanced computer vision, you will surely come across convolutional neural networks, or CNNs, somewhere along the way. Today, this CNN technology There is a lot of software that uses it. Different versions of Yolo and RCNN software can be examples. Although you don't need to have any knowledge of CNNs to use them at a certain level, you need to have a good understanding of the events behind the CNN structure in order to use these neural networks effectively.

In this repo, I will build a convolutional neural network (CNN) example from scratch with the help of the OpenCV library. In the process, you will be able to observe many terms related to neural networks and the mathematical operations that take place behind them at the most basic level. To get the most out of these notes:
- Know Python programming language
- Know the basics of the OpenCV library
- To master basic mathematical operations with matrices

## Folder Structure

```
.
├── Notebooks (EN)                                      # English Notes                                    
│   ├── (not avaliable)            
│   ├── (not avaliable)          
│   ├── (not avaliable)               
│   ├── (not avaliable)                  
│   ├── (not avaliable)                
│   ├── (not avaliable)               
│   ├── (not avaliable) 
│   ├── (not avaliable) 
│   └── (not avaliable) 
├── Notebooks (TR)                                       # Turkish Notes
├── dataset                                              # Dataset storing the images to be used
└── README.md

```
---

# Evrişimsel Sinir Ağlarının Temelleri

Herkese merhaba,
Eğer ileri seviye bilgisayar görüsü ile uğraşmak istiyorsanız yolunuz mutlaka bir yerede evrişimsel sinir ağları yani CNN'ler ile karşılaşacaktır. Günümüzde bu CNN teknolojisini
kullanan bir çok yazılım var. Yolo'nun farklı versionları ve RCNN yazılımıları örnek olabilir. Her ne kadar bunları belirli bir düzeyde kullanmak için CNN'ler ile ilgili herhangi bir bilgiye sahip olmanız gerekmese bile bu nöral ağları efektif kullanmak için CNN yapısının arkasındaki dönen olaylara hakim olmanız gerekmektedir.

Bu repomda OpenCV kütüphanesi yardımı ile sıfırdan bir evrişimsel sinir ağı (CNN) örneği oluşturacağım bu süreçte nöral ağlar ile ilgli bir çok terimi ve arkada gerçekleşen matematiksel işlemleri en temel düzeyde gözlemleyebileceksiniz. Bu notlardan en üst düzey verimi alabilmek için:
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
*Bilgisayarlarlar için resimlerin nasıl göründüğünü, resimler üzerinde nasıl işlem yapabildiklerini ve resimleri nasıl sınıflandırdığını anlamaya çalışacağız. Bunun için de Python programlama dilini kullanarak basit bir sınıflandırıcı oluşturacağız.*

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
