<div align="center">
 
[<kbd> <br> ENGLISH <br> </kbd>][KBD1]
[<kbd> <br> TÜRKÇE <br> </kbd>][KBD2]

</div>

[KBD1]: #basic-understannding-of-convolutional-neural-networks
[KBD2]: #yolov5-tr

***

![Computer vısıon Kopyası (1)](https://user-images.githubusercontent.com/44752389/222967440-09028148-489f-4bef-ae74-6100fe0fef7d.gif)

<br>

<div align="center">
  <img align="left" src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA"/>

  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
  <img src="https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white"/>
  <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white"/>
  <img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white"/>
 
 <img align="right" src="https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green"/>

</div>

***

# YOLOV5 TR
Nesne Tespiti(Object Detection); fotoğraflardaki, videolardaki ve gerçek zamanlı görüntülerdeki nesneleri tespit etmeye odaklanan bilgisayarlı görü ve görüntü işleme ile ilgili bir bilgisayar teknolojisidir. Faster R-CNN, Single Shot Detector (SSD) ve YOLO(You Only Look Once) gibi bir çok nesne tespiti algoritmaları günümüzde kullanılmaktadır. Bu repoda bu algoritalar arasında YoloV5 detaylı olarak incelenecek, tespit ve eğitim algoritmalarının çalışma mantığına bakılacaktır.  

Başlamadan önce YOLO algoritmalarının tarihçesinden bahsetmek istiyorum, YOLO başlangıçta, sınırlayıcı kutu(bounding box) tahmini ve nesne sınıflandırmasını tek bir uçtan uca türevlenebilir ağda birleştiren ilk nesne algılama modeli olarak tanıtıldı. Yani görüntülerdeki veya videolardaki nesneleri ve bu nesnelerin koordinatlarını aynı anda tespit eder. Şu ana kadar yayınlanan YOLO versiyonları Darknet framework üzerinde çalışmaktaydı ancak; YOLOv5 PyTorch framework üzerinde çalışan ilk YOLO modeli oldu. YOLOv5, Glenn Jocher(Founder & CEO of Utralytics) tarafından yayınlandı.

## Repo Yapsı
Bu repo kendimin YoloV5 tespiit algoritmasını anlamak  için kendimce yaptığım testleri ve aldığım notları yaynladığım repodur. Umarım sizlere faydası dokunur. Aşağıda hangi testleri ne amaç ile yazdığımı ve bunun için neler yazdığımı detaylı olarak açıkladım.

### Nesne Tespiti

#### Test 1
YoloV5 ile çalışmaya ilk başladığımda bulduğum bütün rehber ve projeler bir sınıf yapısı halinde bulunan bir algoritma kullanıyordu. Bende bu algoritmayı daha iyi anlamak için sınıf formunda çıkardım ve video ve resim için tespit yapan iki farklı kod dosyası haline getirdim. Bu formuyla tespit algoritmasını satır satır inceleyebildim ve hangi satırın ne amaçla çalıştığını rahatça anlayabildim.  Bahsettiğim sınıf formatındaki tespit algoritmasını main_class.py dosyasının içerisinde bulabilirsiniz. 

#### Test 2
Resimler üzerinde tespit işlemi için oluşturduğum algoritmayı Jupyter Notebook formuna çevirdim ve satır datır üzerinde çalışarak algoritmanın çalışma mantığını daha iyi anladım. Asıl amacım ise sonuçları içinde tutan **results** değişkeninin yapısını öğrenmekti. Bu değişkenin iç yapısısnı daha iyi anlamak için resmi Pythorch dökümanını kullandım ve orada bulunan bir çok methodu deneyerek results değişkenini parçalara ayırdım. Elde ettiğim sonuçları klasörde bulabilirsiniz. Ayrıca kullandığım dökümanda bulunann methodlarıda göseterdiğim ikinci bir not defteri de bulunuyor.

#### Test 3
Tespit algoritmasının yapısını ve çalışma mantığını anladıktan sonra artık algoritmaya kendi eklemelerimi yapabilirim. Kendimi test etmek için tespit edilen cisimin ekaranın hangi tarafında tespit edildiğini döndürecek şekilde algoritmayı güncelledim. Artık algoritma tespit ettiği cisimlerin merkez noktalarının bulunduğu piksellerin sağ, sol, merkez, aşağı veya yukarı bölgelerden hangisinde olduğunu döndüren bir fonksiyona sahip.

### Model Eğitimi
**(not avaliable)**


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
