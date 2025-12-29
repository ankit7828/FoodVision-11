# Food_11_Image_Classifier

This project builds a deep-learning model that classifies food images into 11 different categories using TensorFlow, Keras, and Transfer Learning with MobileNetV2. The dataset is organized into separate training and testing folders, and the model is trained using data augmentation, frozen base layers, and fine-tuning for better accuracy. The final model predicts the food category from an input image and integrated into a Flask web app for easy user interaction and deployment.

Live Demo : https://web-production-19b70.up.railway.app/

# Objective

The objective of this project is to develop an accurate and efficient deep-learning model that can automatically classify food images into 11 categories using Transfer Learning with MobileNetV2. The project aims to demonstrate practical image classification workflows — including data preprocessing, model training, fine-tuning, evaluation, and deployment through a simple web interface — while improving recognition accuracy and making the system lightweight enough for real-world applications.

# Model Performance

The Food-11 classifier was trained using Transfer Learning with MobileNetV2.  

Training Accuracy: 89%  

Test Accuracy: 81%  


These results show that the model generalizes well to unseen data while staying lightweight and efficient. Fine-tuning, data augmentation, and a reduced learning rate helped improve performance and reduce overfitting.

# Installation and Setup
## 1. Clone the repository
git clone https://github.com/ankit7828/Food_11_Image_Classifier
cd Food_11_Image_Classifier  

## 2. Install the dependencies
pip install -r requirements.txt

## 3. Run the Flask app
python app.py

## 4. Open in browser
http://127.0.0.1:5000/

# Datasets Used
## Food11
### 1. Train
### 2. Test
both with 11 categories

food-101/
 ├── images/
 │    ├── pizza/
 │    ├── burger/
 │    ├── sushi/
 │    └── ...
 ├── meta/
 │    ├── train.txt
 │    └── test.txt


Dataset link: https://www.kaggle.com/datasets/imbikramsaha/food11 
These datasets are preprocessed and merged to build a reliable recommendation system.


