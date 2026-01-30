# 📚 Book Buddy: Collaborative Filtering Recommender

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg.svg)](YOUR_STREAMLIT_CLOUD_LINK_HERE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### *Find your next favorite book using the power of Machine Learning.*

**Book Buddy** is a recommendation engine that utilizes **Item-Based Collaborative Filtering** to suggest books based on user behavior patterns. Trained on the "Book-Crossing" dataset, it calculates similarities between thousands of titles to provide accurate, real-time suggestions.

---

## 🚀 Deployment
The application is live! You can try it out here:  
👉 [**[Live Demo Link](YOUR_STREAMLIT_CLOUD_LINK_HERE)**](https://book-buddy2026.streamlit.app/)

---

## 🧠 How the Engine Works

### 1. Data Preprocessing & Sparsity
To ensure the recommendations are based on reliable data, the dataset was filtered:
* **Active Users:** Only users who have provided more than **200 ratings** were considered.
* **Popular Books:** Only books with at least **50 ratings** were included.
This reduced the "noise" and focused the model on established reading trends.

### 2. The Algorithm: K-Nearest Neighbors (KNN)
The system treats each book as a vector in a high-dimensional space where dimensions represent individual users. To find "similar" books, we use the **KNN algorithm** with **Cosine Similarity**.

Unlike standard distance, **Cosine Similarity** measures the angle between two vectors. This is crucial because it captures the *pattern* of ratings rather than just the raw scores.

**The Math:**
The similarity between two book vectors $A$ and $B$ is calculated as:
$$\text{similarity} = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}$$

[Image of Cosine Similarity concept diagram in machine learning]

---

## 🛠️ Tech Stack
* **Core:** Python, Pandas, NumPy
* **ML:** Scikit-Learn (NearestNeighbors)
* **Web Interface:** Streamlit
* **Persistence:** Pickle

---

## 💻 Local Setup

   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
   cd YOUR_REPO_NAME

   python -m venv venv
   source venv/Scripts/activate  # Windows (Git Bash)
   pip install -r requirements.txt
   streamlit run app.py
