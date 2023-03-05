<div align="center">
 
[<kbd> <br> ENGLISH <br> </kbd>][KBD1]
[<kbd> <br> TÜRKÇE <br> </kbd>][KBD2]

</div>

***

[KBD1]: #basic-understannding-of-convolutional-neural-networks
[KBD2]: #evrişimsel-sinir-ağlarının-temelleri

![Computer vısıon Kopyası](https://user-images.githubusercontent.com/44752389/222967264-c171f52d-cf6c-4669-a5c9-894d1f260c81.gif)

<div align="center">
  <img align="left" src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA"/>

  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
  <img src="https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white"/>
  <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white"/>
  <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white"/>
 
 <img align="right" src="https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green"/>

</div>

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

## Achievements
#### 1. Simple Image classifier
> In this notebook we will look at how computers recognize images, how mathematical operations can be performed on images and how images can be classified. Then we will code a simple classifier to distinguish between images containing vertical and horizontal lines.

### 2. Automatic Image Classifier
> In this notebook, we will make the filter of the classifier created in the previous notes automatically adjustable with the help of the Numpy library. The computer will try different filters until it finds a suitable match.

### 3. Let's Create a Simple CNN
> In this notebook we will take a brief look at convolutional neural networks and start building our own network a little bit by little. Towards this goal we will explore the definition of convolution, activation function, weights and thresholds.

### 3.1 Let's Experiment with our Neural Network
> In this code file, you can observe the use of the CNN structure we created in the previous notes as a script by moving it to the pyhon code file. Note: Our network is not yet able to distinguish images, so if you run it, it will not be able to classify the images correctly.

### 4. Let's set the weights
> In this notebook we will look at the math behind readjusting the weights. We will then put this math into lines by writing the code to readjust our weights according to the image with the vertical line. 

### 5. Labels and Datatags
> In this notebook we will perform the weight adjustment we did in the previous section using both images. At the same time, we will learn the term epoch and write a code that will train as many rounds as we want with the help of a loop.

### 6. Create our functions
> In this notebook we will learn the terms forward propagation and back propagation, and we will put the work we did in the last notebook into functions accordingly.

## 6.1 Let's Experiment with our Neural Network
> This script is a test script where we can try the functions created in the previous notes.

### 7. Create our first layer
> In this notebook we will look at the term layer and create a layer for our network by combining the functions we have created into a class. We will then use this class to train our weights.

### 8. Test the Neural Network
> In this notebook we will create a test case to measure the accuracy of the trained weights. We will discuss what to look for when training a model and the problems that can occur if you overtrain the weights.

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
├── Notebooks (EN)                                      
├── Notebooks (TR)                                      
│   ├── 1. Basit Resim sınıflandırıcı.ipynb             
│   ├── 2. Otomatik Resim Sınıflandırıcı.ipynb          
│   ├── 3. Basit Bir CNN Oluşturalım.ipynb              
│   ├── 3.1 Nöral Ağımızı Deneyelim.py                  
│   ├── 4. Ağırlıkları Ayarlayalım.ipynb                
│   ├── 5. Etiketler ve Verisetleri.ipynb               
│   ├── 6. Fonksiyonlarımızı Oluşturalım.ipynb          
│   ├── 6.1 Nöral Ağımızı Deneyelim.py                  
│   ├── 7. İlk Katmanımızı Oluşturalım.ipynb            
│   ├── 8. Nöral Ağı Test Edelim.ipynb                  
│   └── (yüklenmedi)
├── dataset                                              
└── README.md

```

## Kazanımlar
### 1. Basit Resim sınıflandırıcı
> Bu not defterinde bilgisayarların resimleri nasıl algıladığına, resimler üzerinde nasıl matematiksel işlem yapılabildiğine ve resimleri nasıl sınıflandırılabilceğine bakılacaktır. Sonrasında dikey ve yatay çizgiyi içeren resimleri birbirinden ayıracak basit bir sınıflandırıcı ile konu koda dökülecektir.

### 2. Otomatik Resim Sınıflandırıcı
> Bu not defterinde bir önceki notlarda oluşturulan sınıflandırcının filtresini Numpy kütüphanesi yardımı ile otomatik ayarlanabilir hale getireceğiz. Bilgisayar uygun bir eşleşme bulana kadar farklı farklı filtreler deneyerek sonuca ulaşacak.

### 3. Basit Bir CNN Oluşturalım
> Bu not defterinde evrişimsel sinir ağlarına ufak bir bakış yapacağız ve kendi ağımızı ufak ufak oluşturmaya başlayacağız. Bu hedef doğrultusunda konvolüsyon tanımını, aktivasyon fonksiyonu, ağırlık (weights) ve eşik değer kavramlarını iredeleyeceğiz.

### 3.1 Nöral Ağımızı Deneyelim
> Bu kod dosyasında bir önceki notlarda oluşturduğumuz CNN yapısını pyhon kod dosyasına taşıyarak script olarak kullanımını gözlemleyebilirsiniz. Not : Ağımız henüz resimleri ayırt edemiyor o yüzden çalıştırmanız durumunda reimleri doğru sınıflandıramayacaktır.

### 4. Ağırlıkları Ayarlayalım
> Bu not defterinde ağırlıkları yeniden ayarlanmasının arkasındaiki matematiğe bakacağız. Sonrasında bu matematiği ağırlılarımızı dikey çizgi içeren resime göre yeniden ayarlayacak kodları yazarak satırlara dökeceğiz. 

### 5. Etiketler ve Verisetleri
> Bu not defterinde bir önceki bölümde yaptığımız ağırlık ayarlama işlemini her iki resimi de kullanarak gerçekleştireceğiz. Aynı zamanda epoch terimini öğrenecek ve bir döngü yardımıyla istediğimiz tur kadar eğitim yapacak bir kod yazacağız.

### 6. Fonksiyonlarımızı Oluşturalım
> Bu not defterinde forward porpagation ve back propagation terimlrini öğrenecek, geçtiğimiz not defterinde yaptığımız işlerleri uygun şekilde fonksiyonlara yerleştireceğiz.

### 6.1 Nöral Ağımızı Deneyelim
> Bu kod dosyası bir önceki notlarda oluşturulan fonksiyonları deneyebileceğimiz bir deneme scripti'dir.

### 7. İlk Katmanımızı Oluşturalım
> Bu not defterinde katman terimine bakacağız ve oluştuduğumuz fonksiyonları bir sınıf çatısı altında birleştirerek ağımız için bir katman oluşturacağız. Sonrasında bu sınıfı kullanarak ağırıklarımızı eğiteceğiz.

### 8. Nöral Ağı Test Edelim
> Bu not defterinde eğitilen ağırlıkların doğruluğunu ölçeceğimiz test senaryosunu oluşturacağız. Bir modeli eğitirken nelere dikkat edilmesi gerektiğini, ağırlıkları fazla eğitirsen oluşabilcek sorunları konuşacağız.

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
