from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Dataset: [Monthly Spending (KES), Monthly Visits]
data = [
    [1000, 2],
    [1500, 3],
    [2000, 2],
    [5000, 6],
    [6000, 7],
    [5500, 5],
    [12000, 12],
    [15000, 14],
    [13000, 11],
    [3000, 4]
]

# Scale the features
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Create K-Means model
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

# Train the model
kmeans.fit(scaled_data)

# Display cluster assigned to each customer
labels = kmeans.labels_
for i in range(len(data)):
    print(f"Customer {i+1} belongs to Cluster {labels[i]}")

# Display total number of customers in each cluster
print()
for cluster_id in range(3):
    count = list(labels).count(cluster_id)
    print(f"Cluster {cluster_id}: {count} customers")

# --- BONUS TASK: Scatter plot with different colours ---
plt.figure()

# Plot each cluster in different colour
for cluster_id in range(3):
    cluster_points = [data[i] for i in range(len(data)) if labels[i] == cluster_id]
    spending = [p[0] for p in cluster_points]
    visits = [p[1] for p in cluster_points]
    plt.scatter(spending, visits, label=f'Cluster {cluster_id}', s=100)

plt.xlabel("Monthly Spending (KES)")
plt.ylabel("Monthly Visits")
plt.title("Customer Segmentation (K=3)")
plt.legend()
plt.grid(True)
plt.savefig("customer_clusters.png")
plt.show()