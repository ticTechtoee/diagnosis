import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

IMAGE_SIZE = (224, 224)

def load_data(data_dir):
    labels = ['COVID', 'Non-COVID', 'Pneumonia']
    images = []
    targets = []

    for label in labels:
        path = os.path.join(data_dir, label)
        class_num = labels.index(label)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                img_array = cv2.resize(img_array, IMAGE_SIZE)
                images.append(img_array)
                targets.append(class_num)
            except Exception as e:
                pass

    images = np.array(images).reshape(-1, IMAGE_SIZE[0], IMAGE_SIZE[1], 1)
    targets = np.array(targets)
    return images, targets

def preprocess_data(data_dir):
    images, targets = load_data(data_dir)
    images = images / 255.0  # Normalize
    X_train, X_test, y_train, y_test = train_test_split(images, targets, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

if __name__ == '__main__':
    data_dir = "D:\\Development\\Moiz\\source\\u\\dataset"
    X_train, X_test, y_train, y_test = preprocess_data(data_dir)
    np.save('X_train.npy', X_train)
    np.save('X_test.npy', X_test)
    np.save('y_train.npy', y_train)
    np.save('y_test.npy', y_test)



