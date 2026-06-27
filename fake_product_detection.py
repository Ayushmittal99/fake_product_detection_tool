import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

# Load Dataset
df = pd.read_csv(
    r"C:\Users\mitta\OneDrive\Desktop\fake_product_detection\product.csv"
)

# Features for Clustering
features = [
    "Listed_Price",
    "Rating",
    "Reviews_Count",
    "Seller_Score"
]

X = df[features]

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply DBSCAN
dbscan = DBSCAN(
    eps=1.5,
    min_samples=2
)

clusters = dbscan.fit_predict(X_scaled)

# Add Cluster Column
df["Cluster"] = clusters

# Create Status Column
# Cluster 1 contains suspicious products in this dataset
df["Status"] = np.where(
    df["Cluster"] == 1,
    "Suspicious",
    "Genuine"
)

# Display Final Results
print("\nFinal Results:\n")

print(df[[
    "Product_ID",
    "Product_Name",
    "Actual_Market_Price",
    "Listed_Price",
    "Rating",
    "Reviews_Count",
    "Seller_Score",
    "Status"
]])

# Save Results
df.to_csv(
    "fake_product_detection_result.csv",
    index=False
)

print("\nResults saved successfully!")