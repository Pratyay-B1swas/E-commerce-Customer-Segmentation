# 📈 E-commerce Customer Segmentation using RFM and K-Means Clustering

## Project Overview
This project focuses on performing **Customer Segmentation** for an e-commerce retailer to identify distinct customer groups. By understanding customer behavior based on their transaction history, targeted marketing strategies can be developed to maximize customer lifetime value (CLV) and optimize marketing budget allocation.
The primary technique used is **RFM Analysis** (Recency, Frequency, Monetary) followed by **K-Means Clustering**, a powerful unsupervised machine learning algorithm.

## 🚀 Key Features & Methodology
### 1. Data Source
* **Dataset:** Online Retail Dataset (Publicly available transaction data).

### 2. Analytical Approach
| Stage | Goal | Key Technique |
| **Data Preparation** | Clean raw data and compute behavioral metrics. | Removing canceled transactions, handling missing IDs, creating **TotalPrice** column. |
| **RFM Calculation** | Assign a score to each customer based on their purchasing habits. | Calculating **Recency** (days since last purchase), **Frequency** (total transactions), and **Monetary** (total spend). |
| **Data Preprocessing** | Prepare the skewed RFM data for clustering. | **Log Transformation** to normalize data skewness, followed by **Standard Scaling** to ensure equal weighting during clustering. |
| **K-Means Clustering** | Automatically group customers into segments. | **Elbow Method** to find the optimal number of clusters (K), resulting in **K=4**. |

## 📊 Results and Business Insights
The K-Means model successfully identified **4 distinct customer segments**. The analysis of the average RFM values for each cluster provides clear actionable insights:
### Cluster Analysis (Based on Avg RFM Values)
| Cluster Label | Avg Recency (R) | Avg Frequency (F) | Avg Monetary (M) | Segment Name | Actionable Marketing Strategy |
| :---: | :---: | :---: | :---: | :--- | :--- |
| **0** | ~71 Days | ~4 Orders | **~$8074** | **Potential Loyalists** | These customers are the highest spenders but are becoming inactive. **Strategy:** Implement a personalized "Win-Back" campaign with exclusive offers to prevent churn. |
| **1** | **~4 Days** | **~7 Orders** | ~$552 | **New Loyalists** | Recently acquired and highly active. **Strategy:** Nurture them with excellent customer service and incentivize subscription/loyalty programs to secure long-term commitment. |
| **3** | **~182 Days** | ~1 Order | ~$343 | **At Risk/Lost Customers** | High Recency suggests they are close to churning. **Strategy:** Aggressive re-engagement campaign (e.g., deep discounts, free shipping) focused on bringing them back immediately. |
| **2** | ~18 Days | ~2 Orders | ~$181 | **New/Single Buyers** | Recently purchased but low frequency/monetary value. **Strategy:** Focus on product education and cross-selling to convert them into regular buyers. |

### Visualizations
The clustering result is clearly visualized using the RFM metrics.
1.  **Elbow Method Chart:** Used to justify the selection of $K=4$. [Image of Elbow Method for Optimal K chart]
2.  **Segmentation Plot (Recency vs. Monetary):** Shows the clear separation of the 4 segments, highlighting that clusters are grouped by both how recently they bought and how much they spent. 

## 🛠️ How to Run the Project

### Prerequisites
* Python 3.x
* The following libraries:
    ```bash
    pip install pandas numpy datetime scikit-learn matplotlib seaborn openpyxl
### Execution
1.  **Download Data:** Place the `Online Retail.xlsx` file in the project directory.
2.  **RFM Calculation:** Run the first script to calculate RFM scores.
    ```bash
    python rfm_analyser.py
3.  **Clustering:** Run the second script to perform K-Means clustering and generate the final plots (`elbow_method_chart.png` and `rfm_segmentation_plot.png`).
    ```bash
    python rfm_clustering.py
