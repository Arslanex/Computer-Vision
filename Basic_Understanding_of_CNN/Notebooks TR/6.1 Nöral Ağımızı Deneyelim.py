import cv2 as cv
import numpy as np

def prepare_the_image(imgPath):
    img = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)
    img = img / 255
    flatten = img.flatten()
    return flatten

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_der(x):
    return sigmoid(x) * (1 - sigmoid(x))


def feed_forward(input, weights):
    convolution = np.dot(input, weights)
    result = sigmoid(convolution)
    return result

def back_propagation(result, label, input):
    error = abs(result - label)
    adjustment = error * sigmoid_der(result)
    weightUpdate = np.dot(input.T, adjustment)
    return weightUpdate


def neural_network(dataset, labels, epoch=5):
    weights = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])

    for i in range(epoch):
        result = feed_forward(dataset, weights)
        weights -= back_propagation(result, labels, dataset)

        print("\nEPOCH:",i)
        print("Weights", weights)



flattenV = prepare_the_image("../dataset/train/vertical.png")
flattenH = prepare_the_image("../dataset/train/horizontal.png")

dataset = np.array([flattenV, flattenH])
labels = np.array([0,1]).T

neural_network(dataset, labels)