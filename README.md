# Customer Segmentation using K-Means Clustering

## 📌 Project Overview

This project implements the **K-Means Clustering Algorithm**, an unsupervised machine learning technique used to group similar data points into clusters. The project uses the **Mall Customers Dataset** to segment customers based on their **Annual Income** and **Spending Score**.

Customer segmentation helps businesses understand different customer groups and create targeted marketing strategies.

---

## 🎯 Objective

To classify mall customers into distinct groups based on their purchasing behavior using K-Means Clustering.

---

## 📊 Dataset Information

The dataset contains the following attributes:

* CustomerID
* Gender
* Age
* Annual Income (k$)
* Spending Score (1–100)

Total Records: **200 Customers**

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

## 📋 Project Workflow

### 1. Data Loading

Loaded the Mall Customers dataset using Pandas.

### 2. Data Exploration

* Displayed dataset information
* Checked data types
* Generated summary statistics

### 3. Feature Selection

Selected:

* Annual Income (k$)
* Spending Score (1–100)

These features were used for clustering.

### 4. K-Means Clustering

* Applied K-Means algorithm
* Set the number of clusters (K = 5)
* Trained the model on customer data

### 5. Cluster Assignment

Assigned each customer to a cluster based on similarity.

### 6. Data Visualization

Visualized:

* Customer clusters
* Cluster centroids
* Customer distribution patterns

---

## 📈 Results

The algorithm successfully grouped customers into **five distinct segments**:

1. High Income – High Spending
2. High Income – Low Spending
3. Low Income – High Spending
4. Low Income – Low Spending
5. Average Income – Average Spending

Cluster centroids represent the center point of each customer group.

---

## 📷 Output

The final visualization displays:

* Different customer clusters using distinct colors
* Cluster centroids marked with black "X" symbols

---

## 🎓 Learning Outcomes

Through this project, I learned:

* Fundamentals of Unsupervised Machine Learning
* Working with real-world datasets
* Customer Segmentation techniques
* K-Means Clustering Algorithm
* Data Visualization using Matplotlib
* Feature Selection and Analysis

---

## 🚀 Future Improvements

* Determine the optimal K value using the Elbow Method
* Apply feature scaling
* Experiment with other clustering algorithms
* Build an interactive dashboard for visualization

---

## 👩‍💻 Author

**E. Logeswari**
B.E. Robotics and Automation
Machine Learning Internship Project
