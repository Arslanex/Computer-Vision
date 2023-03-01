<div align="center">
 
[<kbd> <br> ENGLISH <br> </kbd>][KBD1]
[<kbd> <br> TÜRKÇE <br> </kbd>][KBD2]

</div>

[KBD1]: #basic-understannding-of-convolutional-neural-networks
[KBD2]: #evrişimsel-sinir-ağlarının-temelleri

<p align="center">
  <img src="https://miro.medium.com/max/1400/1*5b45PD3TTlxN221xKbhMsw.png" width="100%"/>
</p>

***

# YOLOV5 - TR
Nesne Tespiti(Object Detection); fotoğraflardaki, videolardaki ve gerçek zamanlı görüntülerdeki nesneleri tespit etmeye odaklanan bilgisayarlı görü ve görüntü işleme ile ilgili bir bilgisayar teknolojisidir. Faster R-CNN, Single Shot Detector (SSD) ve YOLO(You Only Look Once) gibi bir çok nesne tespiti algoritmaları günümüzde kullanılmaktadır. Bu repoda bu algoritalar arasında YoloV5 detaylı olarak incelenecek, tespit ve eğitim algoritmalarının çalışma mantığına bakılacaktır.  

Başlamadan önce YOLO algoritmalarının tarihçesinden bahsetmek istiyorum, YOLO başlangıçta, sınırlayıcı kutu(bounding box) tahmini ve nesne sınıflandırmasını tek bir uçtan uca türevlenebilir ağda birleştiren ilk nesne algılama modeli olarak tanıtıldı. Yani görüntülerdeki veya videolardaki nesneleri ve bu nesnelerin koordinatlarını aynı anda tespit eder. Şu ana kadar yayınlanan YOLO versiyonları Darknet framework üzerinde çalışmaktaydı ancak; YOLOv5 PyTorch framework üzerinde çalışan ilk YOLO modeli oldu. YOLOv5, Glenn Jocher(Founder & CEO of Utralytics) tarafından yayınlandı.

## Repo Yapsı
### 1. TEST
YoloV5 için yaygın olarak kullanılan tespit algoritması, main_class.py, sınıf yapısıda olduğu için ilk başta anlaması 
daha doğrusu satır satır incelemesi zor olacağı için bu algoritmayı sınıf yapısından çıkartarak resimler için ve videolar
için çalışır hale getiridim. Bu sayede kodu satır satır takip ederek hangi satırın ne yaptığını daha kolay anlayabildim.
Bu kısımda kabaca tespit algoritmasının çoğunun ne işe yaradığını anlayabilirisiniz. Kendi notlarım klasördeki pdf'nin
içerisinde var.

### 2. TEST
Resimler için tespit yapan algoritmayı jupyter notebook formatına taşıdıktan sonra satır satır çalıştırarak daha 
detaylı bir incelem yapabildim. Burada "results" değişkeninin iç yapısı dışında her şey yerine oturdu. Results yapısını
daha iyi anlamak için internetten ufak bir destek aldım, Pytorch'un resmi sitesinde bulunan bir çok method'u test ederken
results değişkenini de daha detaylı inceledim. YoloV5 ile kullanılabilecek ekstra methodlarda pdf'de blunabilir.

### 3. TEST
Artık algoritmanın nasıl çalıştığını çözdüğümüze göre artık algoritmaya kendi eklemelerimizi yapabiliriz. Bu kapsamda 
ilk olarak tespit edilen objelerin merkez noktalarını döndüren bir fonksiyon ekledim. Sonrasında ise bu merkez noktanın 
ekranın neresinde olduğunu (sağ-sol-orta-yukarı-aşağı) ve etiketinin ne olduğunu döndüren yeni fonksiyonlar ekledim.
