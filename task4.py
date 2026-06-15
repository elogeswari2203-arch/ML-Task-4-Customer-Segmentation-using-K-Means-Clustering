# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("Mall_Customers.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Select features for clustering
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Create K-Means model
kmeans = KMeans(n_clusters=5, random_state=42)

# Train model
kmeans.fit(X)

# Assign cluster labels
df['Cluster'] = kmeans.labels_

# Display clustered data
print("\nClustered Dataset:")
print(df.head())

# Plot customer clusters
plt.figure(figsize=(8, 6))

plt.scatter(
    X['Annual Income (k$)'],
    X['Spending Score (1-100)'],
    c=df['Cluster'],
    cmap='rainbow'
)

# Plot centroids
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    s=250,
    color='black',
    marker='X',
    label='Centroids'
)

# Labels and title
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Customer Segmentation using K-Means Clustering")
plt.legend()

# Show graph
plt.show()