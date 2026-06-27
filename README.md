# 🛒 Fake Product Listing Detection Using DBSCAN

## 📌 Project Overview

Fake and fraudulent product listings are a major challenge for e-commerce platforms. Sellers often manipulate prices, ratings, and reviews to attract customers, making it difficult to identify suspicious products manually.

This project uses the **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** algorithm to automatically detect abnormal product listings without requiring labeled data.

---

## 🚀 Business Problem

Online marketplaces such as **Amazon, Flipkart, Meesho, and Myntra** allow thousands of sellers to upload products every day.

Some sellers create fake or suspicious listings by:

- Offering unrealistic discounts
- Manipulating product ratings
- Creating fake reviews
- Having poor seller credibility
- Selling counterfeit products

Manual verification is expensive and time-consuming. This project aims to automate the detection of suspicious product listings using Machine Learning.

---

## 🎯 Objective

The main objectives of this project are:

- Identify genuine product clusters
- Detect abnormal product listings
- Automatically flag suspicious products
- Reduce fraud-related risks
- Improve customer trust
- Minimize manual verification efforts

---

## 🗂 Dataset Features

| Feature | Description |
|----------|-------------|
| Product_ID | Unique Product Identifier |
| Product_Name | Product Name |
| Actual_Market_Price | Expected Market Price |
| Listed_Price | Seller Listed Price |
| Rating | Product Rating |
| Reviews_Count | Number of Reviews |
| Seller_Score | Seller Reputation Score |

---

## 🧠 Why DBSCAN?

Unlike supervised learning algorithms, DBSCAN does not require labeled data.

### Advantages

- No need to specify the number of clusters
- Detects outliers automatically
- Works well for anomaly detection
- Handles arbitrary-shaped clusters
- Suitable for fraud detection problems

---

## ⚙️ Machine Learning Workflow

```
Data Collection
        │
        ▼
Data Cleaning
        │
        ▼
Feature Selection
        │
        ▼
Feature Scaling
        │
        ▼
DBSCAN Clustering
        │
        ▼
Cluster Identification
        │
        ▼
Noise Detection (-1)
        │
        ▼
Suspicious Product Detection
```

---

## 📊 Features Used for Clustering

The following numerical features were used:

- Listed Price
- Rating
- Reviews Count
- Seller Score

These features help identify unusual seller behavior and suspicious listings.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- DBSCAN
- StandardScaler
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## 📈 Results

The DBSCAN model successfully identified:

- Genuine product clusters
- Suspicious product listings
- Outlier products using the **Noise (-1)** label

Products with:

- Extremely low prices
- Very few reviews
- Poor seller scores
- Unusually high ratings

were automatically flagged as suspicious.

---

## 💼 Business Impact

This solution can help e-commerce companies:

- Reduce fake product listings
- Improve marketplace quality
- Increase customer trust
- Reduce manual investigation costs
- Detect emerging fraud patterns

---

## 📂 Project Structure

```
fake_product_detection_tool/
│
├── data/
│   ├── products.csv
│
├── notebooks/
│   ├── Fake_Product_Detection.ipynb
│
├── images/
│   ├── dbscan_clusters.png
│   ├── workflow.png
│
├── requirements.txt
├── README.md
└── fake_product_detection.py
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/Ayushmittal99/fake_product_detection_tool.git
```

Move into the project directory

```bash
cd fake_product_detection_tool
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python fake_product_detection.py
```

---

## 📌 Future Improvements

- Deploy the model using Streamlit
- Real-time fraud detection
- Hyperparameter optimization
- Integration with e-commerce platforms
- Add Isolation Forest and Local Outlier Factor for comparison

---

## 👨‍💻 Author

**Ayush Mittal**

📧 Email: mittalayush520@gmail.com

🔗 LinkedIn: https://linkedin.com/in/ayush-mittal-b6b9ab364

💻 GitHub: https://github.com/Ayushmittal99

---

## ⭐ If you found this project useful, consider giving it a Star!
