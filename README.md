# 🕵️‍♀️ Fake Review Detection Using NLP and Machine Learning

Detect whether a product review is **fake** or **genuine** using Natural Language Processing and a trained machine learning model. Built with Python, Scikit-learn, and Streamlit for interactive prediction and visualization.

![Streamlit UI](https://img.shields.io/badge/Made%20With-Streamlit-red?logo=streamlit)

---

## 📌 Project Overview

This project aims to identify fake product reviews using:
- 🧹 Text preprocessing (cleaning, stemming, stopword removal)
- ✍️ TF-IDF vectorization
- 🧠 Naive Bayes classification
- 📈 Data visualization
- 💻 Web interface with Streamlit

---

## 🎯 Features

- Live prediction of review authenticity  
- TF-IDF + Naive Bayes pipeline  
- Beautiful visualizations: heatmaps, bar charts, histograms  
- Cleaned CSV output  
- Streamlit web interface  
- Ready for deployment 🚀

---

## 📊 Dataset

We use a **Kaggle dataset** containing two files:

- `True.csv` → Genuine reviews  
- `Fake.csv` → Artificial/fake reviews  

Both datasets are:
- Labeled: `0 = Genuine`, `1 = Fake`
- Combined and cleaned using NLP techniques
- Exported as `cleaned_reviews.csv`

---

## 🧠 Machine Learning Model

- **Text Preprocessing**: Lowercasing, removing punctuation, stopwords, stemming
- **Vectorization**: TF-IDF
- **Classifier**: Multinomial Naive Bayes

Model and vectorizer are saved as:
- `model.pkl`
- `vectorizer.pkl`

---

## 📁 Project Structure
Fake-Review-Detector
* app.py # Streamlit app
* model.pkl # Trained model
* vectorizer.pkl # TF-IDF vectorizer
* True.csv / fake.csv # Original datasets
* README.md # Project details

---

## ✨ What You Can Do
* Paste a review → Click “Check” → Get prediction
* See real-time results: Fake or Genuine
* Review visualizations: heatmap, word cloud, bar chart

---

## 📈 Visualizations Included
* Bar Plot – Distribution of fake vs real reviews
* Line Chart – Word count per review
* Heatmap – Correlation matrix
* Histogram – Review length
* WordCloud – Most frequent words in fake/genuine reviews

---

## 🧠 Future Improvements
* Add deep learning model (LSTM / BERT)
* Support multi-lingual reviews
* Connect to live product review sites (e.g., Amazon)
* Add admin panel for flagged reviews

---

## 📃 License
This project is licensed under the MIT License – see the LICENSE file for details.
