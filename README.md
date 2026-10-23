**Name:** Nancy

## Project Title
MaMachine Learning Projects - Supervised & Unsupervised

## Description of the Supervised Learning Project

**File:** `supervised_ml.py`

This project uses **Linear Regression** to predict exam scores based on hours studied.


## Description of the Unsupervised Learning Project

**File:** `unsupervised_ml.py`

This project uses **K-Means Clustering (K=3)** to segment customers.

## Instructions for Installing Dependencies and Running Your Code
To install depedencies run this command on your terminal
-pip install scikit-learn
-pip install scikit-learn matplotlib
To run the code run this on your terminal
-python supervised_ml.py
-Enter hours studied: (any of your choice)
-python unsupervised_ml.py

## Theory Questions

## 1. What is supervised machine learning?
Supervised learning is a type of machine learning where the model is trained on labeled data. It looks on the pattern of data.

## 2. What is unsupervised machine learning?
Unsupervised learning is where the model is trained on unlabeled data. Uses clustered grouping related data.

## 3. Explain the difference between supervised and unsupervised learning.
-In Supervised we use labeled data like (x and y) while in unsupervised we use unlabeled data
-In supervised it main goal is to predict an output while in Unsupervised it Goal is to find hidden patterns/groups.

### 4. Why is Linear Regression considered supervised learning?
Linear Regression considered supervised because it learns from labeled data.

### 5. Why is K-Means considered unsupervised learning?
K-Means considered unsupervised because it works on unlabeled data anddoes not require pre-defined target answer or class labels during training.

### 6. What is the difference between fit() and predict()?
-fix() Teachers the model by analyzing training data(x features and y labels).
-It calculates internal parameter, weights or statistical properties.
-predict() Uses the knowledge and learned parameters obtained during fit() to generate output.
-It applies the saved model parameter to new, unseen data.

### 7. Give two real-world applications of supervised learning and two of unsupervised learning.

**Supervised Learning:**
1. Email Spam Filtering
-Whereby the algorithm is trained on a labeled dataset of emails marked as either (spam or not spam)
-In real-world the Email provider like Gmail uses these trained models to inspect incoming message for specific trigger words, sender addresses and structural pattern. And automatically moves unwanted junk mail into the spam folder.
2. Credit Card Fraud Detection
- The model learns from historical transaction data labeled as legitimate orfraudulent bsed on past users eg: purchase amount or geographic locations.
- In rear-world the Financial Institution run real-time supervised learning models on every swipe or any purchase to flag or block suspicious transaction before money is lost.

**Unsupervised Learning:**
1. Customer Segmentation in Retail 
- clustering algorithms like K-Means groups shoppers based on purchsing history, browsing behaviour and site activity without predefined categories
- In real-world Retailers uses these groupto design targeted markerting campaigns, loyalty programs and promotion offers.
2. News Topic Modelling and Categorization
-  Algorithm analyze large volume of unsructured text to discover naturalconnection and group simillar documents together.
- In real-world Platform like Google News uses these techinique to automatically categorize articles covering the exact same event or story from different publishers