import cv2 as cv
import numpy as np

def prepare_the_image(imgPath):
    img = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)
    img = img/255
    flatten = img.flatten()
    return flatten

def sigmoid(x):
    return 1/(1+np.exp(-x))

def neural_network(img_path):
    weights = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
    convolution = sum(prepare_the_image(img_path) * weights)
    result = sigmoid(convolution)
    if result < 0.5:
        return  "Image is VERTICAL"
    elif result > 0.5:
        return "Image is HORIZONTAL"

"""
Henüz ağırlılar doğru değerler sahip olmadığı için iki 
resim arasındaki farkı anlayamayacaktır. Sadece script
olarak yazılma şekline göstermek istedim.
"""

print(neural_network("../dataset/train/vertical.png"))
print(neural_network("../dataset/train/horizontal.png"))

