import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

INPUT_FILE = "rfm_scores.csv" 
print(f"Starting K-Means Clustering on: {INPUT_FILE}")
try:
    rfm_df = pd.read_csv(INPUT_FILE)
except FileNotFoundError:
    print(f"Error: File not found. Please make sure {INPUT_FILE} is in the same folder.")
    exit()

rfm_df.columns = rfm_df.columns.str.lower()
RFM_COLS = ['recency', 'frequency', 'monetary']
rfm_data = rfm_df[RFM_COLS]
print("Data successfully loaded and columns standardized.")
rfm_log = rfm_data.apply(lambda x: np.log(x + 1), axis=1)
rfm_log.columns = ['recency', 'frequency', 'monetary'] 
print("Data Log-Transformed.")

scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm_log)
rfm_scaled_df = pd.DataFrame(rfm_scaled, columns=['recency_scaled', 'frequency_scaled', 'monetary_scaled'])

sse = {} 
print("Running Elbow Method...")
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(rfm_scaled_df)
    sse[k] = kmeans.inertia_
plt.figure(figsize=(10, 6))
plt.plot(list(sse.keys()), list(sse.values()), marker='o')
plt.title('Elbow Method for Optimal K', fontsize=15)
plt.xlabel('Number of Clusters (K)')
plt.ylabel('SSE (Inertia)')
plt.savefig('elbow_method_chart.png')
FINAL_K = 4 
kmeans = KMeans(n_clusters=FINAL_K, random_state=42, n_init=10)
kmeans.fit(rfm_scaled_df)
rfm_df['cluster_label'] = kmeans.labels_
print(f"\nK-Means Clustering Complete with K={FINAL_K}.")

cluster_analysis = rfm_df.groupby('cluster_label').agg(
    Avg_Recency=('recency', 'mean'),
    Avg_Frequency=('frequency', 'mean'),
    Avg_Monetary=('monetary', 'mean'),
    Count=('customerid', 'size') 
).sort_values(by='Avg_Monetary', ascending=False)

print("\nCluster Characteristics (Avg RFM Values):")
print(cluster_analysis)
plt.figure(figsize=(12, 8))
sns.scatterplot(
    x=rfm_log['recency'], 
    y=rfm_log['monetary'], 
    hue=rfm_df['cluster_label'], 
    palette='viridis', 
    size=rfm_log['frequency'], 
    sizes=(20, 200),
    legend='full'
)
plt.title('Customer Segmentation (Log Transformed Recency vs Monetary)', fontsize=16)
plt.xlabel('Log(Recency)')
plt.ylabel('Log(Monetary)')
plt.legend(title='Cluster Label', loc='best')

plt.savefig('rfm_segmentation_plot.png')
print("✅ Final Segmentation Plot saved as: rfm_segmentation_plot.png")
rfm_df.to_csv('rfm_analyzed_data.csv', index=False)
print("Analyzed data saved to: rfm_analyzed_data.csv")
