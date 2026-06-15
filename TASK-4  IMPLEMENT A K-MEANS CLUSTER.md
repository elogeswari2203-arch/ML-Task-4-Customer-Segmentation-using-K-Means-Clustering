## **TASK-4 : IMPLEMENT A K-MEANS CLUSTERING ALGORITHM**



===========================================================



1\. WHAT IS CLUSTERING?

&#x20;  ===========================================================



Clustering means:



```

Grouping similar data points together automatically.

```



Example:



```

Students with similar marks can be grouped together.



High Scorers

Average Scorers

Low Scorers

```



Machine Learning finds these groups automatically.



\---



Clustering belongs to:



```

UNSUPERVISED LEARNING

```



Reason:



```

No target/output column is given.

```



\---



Example:



```

Customer Data



Income

Spending Score

```



Machine Learning groups customers based on similarities.



===========================================================

2\. WHAT IS K-MEANS?

===================



K-Means is a Machine Learning algorithm used for:



```

\- Clustering

\- Data Segmentation

\- Finding Similar Groups

```



Purpose:



```

Divide data into K clusters.

```



Example:



```

K = 5

```



Means:



```

Create 5 groups.

```



\---



K-Means tries to:



```

Put similar data points together

Separate different data points

```



===========================================================

3\. WHAT IS THE MALL CUSTOMER DATASET?

=====================================



Dataset contains customer information.



Columns:



```

CustomerID

Gender

Age

Annual Income (k$)

Spending Score (1-100)

```



Meaning:



```

Annual Income

&#x20;   Customer income



Spending Score

&#x20;   How much customer spends

```



Goal:



```

Group customers with similar spending behavior.

```



===========================================================

4\. IMPORT LIBRARIES

===================



Code:



```

import pandas as pd

import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

```



\---



(i) What is Pandas?



```

Pandas is a library used for:



&#x20;   - Reading datasets

&#x20;   - Tables

&#x20;   - Data analysis

```



Short form:



```

pd

```



\---



(ii) What is Matplotlib?



```

Used for:



&#x20;   - Graphs

&#x20;   - Charts

&#x20;   - Visualization

```



Short form:



```

plt

```



\---



(iii) What is sklearn?



Full form:



```

Scikit-Learn

```



Machine Learning library used for:



```

\- Regression

\- Classification

\- Clustering

```



\---



(iv) What is KMeans?



```

Clustering algorithm provided by sklearn.

```



===========================================================

5\. LOAD DATASET

===============



Code:



```

df = pd.read\_csv("Mall\_Customers.csv")

```



\---



What is happening?



```

Pandas reads CSV file.



Converts dataset into table format.

```



\---



What is df?



```

df = DataFrame

```



Think of it like:



```

Excel Sheet inside Python

```



===========================================================

6\. DISPLAY FIRST 5 ROWS

=======================



Code:



```

print(df.head())

```



\---



What is head()?



Shows:



```

First 5 rows of dataset.

```



Useful for:



```

Checking data quickly.

```



===========================================================

7\. DATASET INFORMATION

======================



Code:



```

print(df.info())

```



\---



info() shows:



```

\- Number of rows

\- Number of columns

\- Data types

\- Memory usage

```



Example Output:



```

Rows = 200

Columns = 5

```



===========================================================

8\. SUMMARY STATISTICS

=====================



Code:



```

print(df.describe())

```



\---



describe() calculates:



```

\- Count

\- Mean

\- Standard Deviation

\- Minimum

\- Maximum

\- Quartiles

```



Automatically.



\---



Example:



```

Mean Income = 60.56

```



Meaning:



```

Average customer income.

```



===========================================================

9\. SELECT FEATURES

==================



Code:



```

X = df\[\['Annual Income (k$)',

&#x20;       'Spending Score (1-100)']]

```



\---



Why?



Dataset has many columns:



```

CustomerID

Gender

Age

Income

Spending Score

```



For clustering we only use:



```

Income

Spending Score

```



\---



What is X?



Input data used for clustering.



===========================================================

10\. CREATE K-MEANS MODEL

========================



Code:



```

kmeans = KMeans(

&#x20;   n\_clusters=5,

&#x20;   random\_state=42

)

```



\---



What is n\_clusters?



Number of clusters.



Example:



```

n\_clusters = 5

```



Means:



```

Create 5 groups.

```



\---



What is random\_state?



Keeps output same every run.



Without random\_state:



```

Results may slightly change.

```



===========================================================

11\. TRAIN MODEL

===============



Code:



```

kmeans.fit(X)

```



\---



What is fit()?



Trains the model.



\---



What happens internally?



STEP 1:



```

Place K random points.

```



Called:



```

Centroids

```



STEP 2:



```

Find nearest centroid.

```



STEP 3:



```

Assign customer to cluster.

```



STEP 4:



```

Move centroid to center.

```



STEP 5:



```

Repeat until centroids stop moving.

```



This process is called:



```

Convergence

```



===========================================================

12\. WHAT IS A CENTROID?

=======================



Centroid means:



```

Center point of cluster.

```



Example:



```

Values:



40

42

44

```



Center:



```

42

```



This center is called:



```

Centroid

```



===========================================================

13\. ASSIGN CLUSTER LABELS

=========================



Code:



```

df\['Cluster'] = kmeans.labels\_

```



\---



What is labels\_?



After training:



```

K-Means assigns cluster numbers.

```



Example:



```

Customer 1 -> Cluster 2

Customer 2 -> Cluster 0

Customer 3 -> Cluster 4

```



\---



New Column Added:



```

Cluster

```



===========================================================

14\. CREATE CLUSTER PLOT

=======================



Code:



```

plt.scatter(

&#x20;   X\['Annual Income (k$)'],

&#x20;   X\['Spending Score (1-100)'],

&#x20;   c=df\['Cluster'],

&#x20;   cmap='rainbow'

)

```



\---



X-Axis:



```

Annual Income

```



Y-Axis:



```

Spending Score

```



\---



What is c=df\['Cluster'] ?



Colors customers based on cluster.



\---



What is cmap='rainbow' ?



Uses different colors for different clusters.



===========================================================

15\. DISPLAY CENTROIDS

=====================



Code:



```

plt.scatter(

&#x20;   kmeans.cluster\_centers\_\[:,0],

&#x20;   kmeans.cluster\_centers\_\[:,1],

&#x20;   s=250,

&#x20;   color='black',

&#x20;   marker='X',

&#x20;   label='Centroids'

)

```



\---



cluster\_centers\_



Stores centroid coordinates.



\---



\[:,0]



All X values



(Income)



\---



\[:,1]



All Y values



(Spending Score)



\---



marker='X'



Shows centroid as X mark.



\---



color='black'



Black color.



===========================================================

16\. GRAPH LABELS

================



Code:



```

plt.xlabel("Annual Income (k$)")

plt.ylabel("Spending Score (1-100)")

```



\---



Purpose:



```

Label X-axis and Y-axis.

```



===========================================================

17\. GRAPH TITLE

===============



Code:



```

plt.title(

&#x20;   "Customer Segmentation using K-Means Clustering"

)

```



\---



Purpose:



```

Adds heading to graph.

```



===========================================================

18\. LEGEND

==========



Code:



```

plt.legend()

```



\---



Purpose:



```

Displays label:



&#x20;   Centroids

```



===========================================================

19\. SHOW GRAPH

==============



Code:



```

plt.show()

```



\---



Purpose:



```

Display graph window.

```



Without this:



```

Graph may not appear.

```



===========================================================

20\. FINAL OUTPUT ANALYSIS

=========================



Cluster 1:



```

Low Income

High Spending

```



\---



Cluster 2:



```

Low Income

Low Spending

```



\---



Cluster 3:



```

Average Income

Average Spending

```



\---



Cluster 4:



```

High Income

High Spending

```



\---



Cluster 5:



```

High Income

Low Spending

```



===========================================================

21\. INTERVIEW QUESTIONS

=======================



Q1. What is K-Means?



Ans:



```

A clustering algorithm used to group similar data points.

```



\---



Q2. What does K represent?



Ans:



```

Number of clusters.

```



\---



Q3. What is a centroid?



Ans:



```

Center point of a cluster.

```



\---



Q4. Why use K-Means?



Ans:



```

To identify hidden groups in data.

```



\---



Q5. Is K-Means supervised or unsupervised?



Ans:



```

Unsupervised Learning.

```



\---



Q6. Why did we use Annual Income and Spending Score?



Ans:



```

They best represent customer purchasing behavior.

```



===========================================================

22\. WHAT I LEARNED IN TASK 4

============================



✓ Unsupervised Learning



✓ Clustering



✓ K-Means Algorithm



✓ Customer Segmentation



✓ Centroids



✓ Cluster Labels



✓ Data Visualization



✓ Real-world Business Analytics



===========================================================

END OF TASK 4 NOTES

===================



