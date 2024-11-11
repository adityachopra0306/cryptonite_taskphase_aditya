# Implementation of Logistic Regression

## Importing Libraries


```python
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt
%matplotlib inline
```


```python
def sigmoid(z):
    return 1/(1+np.exp(-z))
```

## Loading Data


```python
CSVPATH = 'purchase.csv'
df = pd.read_csv(CSVPATH)
df
```

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>User ID</th>
      <th>Gender</th>
      <th>Age</th>
      <th>EstimatedSalary</th>
      <th>Purchased</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15624510</td>
      <td>Male</td>
      <td>19</td>
      <td>19000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15810944</td>
      <td>Male</td>
      <td>35</td>
      <td>20000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>15668575</td>
      <td>Female</td>
      <td>26</td>
      <td>43000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15603246</td>
      <td>Female</td>
      <td>27</td>
      <td>57000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>15804002</td>
      <td>Male</td>
      <td>19</td>
      <td>76000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>395</th>
      <td>15691863</td>
      <td>Female</td>
      <td>46</td>
      <td>41000</td>
      <td>1</td>
    </tr>
    <tr>
      <th>396</th>
      <td>15706071</td>
      <td>Male</td>
      <td>51</td>
      <td>23000</td>
      <td>1</td>
    </tr>
    <tr>
      <th>397</th>
      <td>15654296</td>
      <td>Female</td>
      <td>50</td>
      <td>20000</td>
      <td>1</td>
    </tr>
    <tr>
      <th>398</th>
      <td>15755018</td>
      <td>Male</td>
      <td>36</td>
      <td>33000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>399</th>
      <td>15594041</td>
      <td>Female</td>
      <td>49</td>
      <td>36000</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>400 rows × 5 columns</p>
</div>




```python
df = df.drop('User ID', axis=1).dropna()
```


```python
df['Gender'] = df['Gender'].replace({'Male':1,'Female':0})
```

## Pre-Processing


```python
dat = df.to_numpy()
np.random.shuffle(dat)
x = dat[:,0:-1]
```


```python
y = dat[:,-1]
```


```python
x_mean = x.mean(axis=0)
x_std = x.std(axis=0)
```


```python
x = x.astype(float)
x[:,1:3] = (x[:,1:3]-x_mean[1:3])/x_std[1:3]
x = np.hstack([np.ones((400,1)),x])
```


```python
l_train, l_test = 320,80
train_x, test_x = x[0:l_train,:], x[l_train:,:]
train_y, test_y = y[0:l_train], y[l_train:]
```

## Training- Batch Gradient Descent


```python
alpha = 0.01
parameters = 3
theta = np.zeros(parameters+1)
prevcost = float('inf')
threshold = 1e-6
```


```python
while True:
    hypothesis = sigmoid(train_x @ theta)
    theta = theta + (alpha / l_train) * (train_x.T @ (train_y - hypothesis))
    currcost = (1 / (2 * l_train)) * np.sum(np.square(train_y-hypothesis))
    if currcost-prevcost <= threshold:
        break
    prevcost = currcost
```

## Testing


```python
test_predictions = sigmoid(test_x @ theta) >= 0.5
accuracy = np.mean(test_predictions == test_y) * 100
print("Test Accuracy:", accuracy, "%")
```

    Test Accuracy: 82.5 %

