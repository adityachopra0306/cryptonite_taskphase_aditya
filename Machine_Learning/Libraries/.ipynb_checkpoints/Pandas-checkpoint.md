# Pandas
Pandas is an essential Python library for data analysis and manipulation. It provides powerful data structures, Series and DataFrame, for handling and analyzing structured data, often sourced from CSV, Excel, SQL databases, or JSON files.

## Features:
Allows easy data manipulation and cleaning.
Provides robust data analysis tools.
Supports handling missing data, grouping, and merging.

The Pandas library needs to be installed through pip, after which it can be imported to a Python Project


```python
import numpy as np
import pandas as pd
```

## Series

1-Dimensional labeled array which can hold data of any type

### Creating a Series

#### 1. From List


```python
s = pd.Series([10,20,30,40,50])
s
```




    0    10
    1    20
    2    30
    3    40
    4    50
    dtype: int64




```python
s[3]
```




    np.int64(40)




```python
#Index arguments
indexargs = ['a','b','c','d','e']
s = pd.Series([10,20,30,40,50], indexargs, dtype='int32')
s
```




    a    10
    b    20
    c    30
    d    40
    e    50
    dtype: int32




```python
s['b']
```




    np.int32(20)



#### 2. From Dictionary


```python
cars = {'Tesla':10, 'Honda':15, 'Audi':20}
d = pd.Series(cars)
d
```




    Tesla    10
    Honda    15
    Audi     20
    dtype: int64



## DataFrames

2-Dimensional labeled array which can hold various columns of potentially different types

### Creating a DataFrame

#### 1. From 2-dimensional array


```python
dat = np.random.rand(4,3)
dat
```




    array([[0.30822284, 0.72665856, 0.50336333],
           [0.06436423, 0.24547411, 0.89591141],
           [0.21452223, 0.80270307, 0.49073515],
           [0.31834176, 0.29887399, 0.67741717]])




```python
rows = ["A","B","C","D"]
cols = ["X","Y","Z"]
```


```python
df = pd.DataFrame(dat, rows, cols)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0.308223</td>
      <td>0.726659</td>
      <td>0.503363</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.064364</td>
      <td>0.245474</td>
      <td>0.895911</td>
    </tr>
    <tr>
      <th>C</th>
      <td>0.214522</td>
      <td>0.802703</td>
      <td>0.490735</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.318342</td>
      <td>0.298874</td>
      <td>0.677417</td>
    </tr>
  </tbody>
</table>
</div>



#### 2. From CSV File


```python
CSVPATH = '../Resources/csvdata.csv'
csvdf = pd.read_csv(CSVPATH)
csvdf
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Roll No</th>
      <th>Marks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>J</td>
      <td>1</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>D</td>
      <td>2</td>
      <td>90</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <th>3</th>
      <td>H</td>
      <td>4</td>
      <td>85</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>5</td>
      <td>32</td>
    </tr>
    <tr>
      <th>5</th>
      <td>K</td>
      <td>6</td>
      <td>44</td>
    </tr>
    <tr>
      <th>6</th>
      <td>B</td>
      <td>7</td>
      <td>99</td>
    </tr>
    <tr>
      <th>7</th>
      <td>G</td>
      <td>8</td>
      <td>100</td>
    </tr>
    <tr>
      <th>8</th>
      <td>I</td>
      <td>9</td>
      <td>22</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A</td>
      <td>10</td>
      <td>60</td>
    </tr>
    <tr>
      <th>10</th>
      <td>F</td>
      <td>11</td>
      <td>57</td>
    </tr>
  </tbody>
</table>
</div>



#### 3. From Excel File


```python
EXCELPATH = '../Resources/exceldata.xlsx'
exceldf = pd.read_excel(EXCELPATH)
exceldf
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Roll No</th>
      <th>Marks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>J</td>
      <td>1</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>D</td>
      <td>2</td>
      <td>90</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <th>3</th>
      <td>H</td>
      <td>4</td>
      <td>85</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>5</td>
      <td>32</td>
    </tr>
    <tr>
      <th>5</th>
      <td>K</td>
      <td>6</td>
      <td>44</td>
    </tr>
    <tr>
      <th>6</th>
      <td>B</td>
      <td>7</td>
      <td>99</td>
    </tr>
    <tr>
      <th>7</th>
      <td>G</td>
      <td>8</td>
      <td>100</td>
    </tr>
    <tr>
      <th>8</th>
      <td>I</td>
      <td>9</td>
      <td>22</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A</td>
      <td>10</td>
      <td>60</td>
    </tr>
    <tr>
      <th>10</th>
      <td>F</td>
      <td>11</td>
      <td>57</td>
    </tr>
  </tbody>
</table>
</div>



### Accessing Data

#### 1. df.head(), df.tail()


```python
#First 5 rows
exceldf.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Roll No</th>
      <th>Marks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>J</td>
      <td>1</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>D</td>
      <td>2</td>
      <td>90</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <th>3</th>
      <td>H</td>
      <td>4</td>
      <td>85</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>5</td>
      <td>32</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Last 3 rows
exceldf.tail(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Roll No</th>
      <th>Marks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>I</td>
      <td>9</td>
      <td>22</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A</td>
      <td>10</td>
      <td>60</td>
    </tr>
    <tr>
      <th>10</th>
      <td>F</td>
      <td>11</td>
      <td>57</td>
    </tr>
  </tbody>
</table>
</div>



#### 2. Direct Access


```python
exceldf['Name']
```




    0     J
    1     D
    2     C
    3     H
    4     E
    5     K
    6     B
    7     G
    8     I
    9     A
    10    F
    Name: Name, dtype: object




```python
exceldf[['Name','Marks']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Marks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>J</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>D</td>
      <td>90</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>70</td>
    </tr>
    <tr>
      <th>3</th>
      <td>H</td>
      <td>85</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>32</td>
    </tr>
    <tr>
      <th>5</th>
      <td>K</td>
      <td>44</td>
    </tr>
    <tr>
      <th>6</th>
      <td>B</td>
      <td>99</td>
    </tr>
    <tr>
      <th>7</th>
      <td>G</td>
      <td>100</td>
    </tr>
    <tr>
      <th>8</th>
      <td>I</td>
      <td>22</td>
    </tr>
    <tr>
      <th>9</th>
      <td>A</td>
      <td>60</td>
    </tr>
    <tr>
      <th>10</th>
      <td>F</td>
      <td>57</td>
    </tr>
  </tbody>
</table>
</div>



#### 3. df.loc[], df.iloc[]


```python
exceldf.loc[0,['Name','Marks']]
```




    Name      J
    Marks    10
    Name: 0, dtype: object




```python
exceldf.loc[[0,1,2,3,4,5],:]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Roll No</th>
      <th>Marks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>J</td>
      <td>1</td>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>D</td>
      <td>2</td>
      <td>90</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>3</td>
      <td>70</td>
    </tr>
    <tr>
      <th>3</th>
      <td>H</td>
      <td>4</td>
      <td>85</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>5</td>
      <td>32</td>
    </tr>
    <tr>
      <th>5</th>
      <td>K</td>
      <td>6</td>
      <td>44</td>
    </tr>
  </tbody>
</table>
</div>




```python
exceldf.iloc[0,[1,2]]
```




    Roll No     1
    Marks      10
    Name: 0, dtype: object




```python
exceldf.iloc[:,2]
```




    0      10
    1      90
    2      70
    3      85
    4      32
    5      44
    6      99
    7     100
    8      22
    9      60
    10     57
    Name: Marks, dtype: int64




```python
exceldf.iloc[3,:]
```




    Name        H
    Roll No     4
    Marks      85
    Name: 3, dtype: object



### Analysing Data

#### 1. Get DataFrame Information


```python
df.columns
```




    Index(['X', 'Y', 'Z'], dtype='object')




```python
df.index
```




    Index(['A', 'B', 'C', 'D'], dtype='object')




```python
df.shape
```




    (4, 3)




```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0.308223</td>
      <td>0.726659</td>
      <td>0.503363</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.064364</td>
      <td>0.245474</td>
      <td>0.895911</td>
    </tr>
    <tr>
      <th>C</th>
      <td>0.214522</td>
      <td>0.802703</td>
      <td>0.490735</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.318342</td>
      <td>0.298874</td>
      <td>0.677417</td>
    </tr>
  </tbody>
</table>
</div>




```python
exceldf.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 11 entries, 0 to 10
    Data columns (total 3 columns):
     #   Column   Non-Null Count  Dtype 
    ---  ------   --------------  ----- 
     0   Name     11 non-null     object
     1   Roll No  11 non-null     int64 
     2   Marks    11 non-null     int64 
    dtypes: int64(2), object(1)
    memory usage: 396.0+ bytes



```python
exceldf.dtypes
```




    Name       object
    Roll No     int64
    Marks       int64
    dtype: object



#### 2. Statistical Analysis


```python
exceldf.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Roll No</th>
      <th>Marks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>11.000000</td>
      <td>11.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>6.000000</td>
      <td>60.818182</td>
    </tr>
    <tr>
      <th>std</th>
      <td>3.316625</td>
      <td>31.195571</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>10.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>3.500000</td>
      <td>38.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>6.000000</td>
      <td>60.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>8.500000</td>
      <td>87.500000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>11.000000</td>
      <td>100.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
exceldf['Name'].describe()
```




    count     11
    unique    11
    top        J
    freq       1
    Name: Name, dtype: object




```python
data = {
    'City': ['A', 'B', None, 'C', 'B', 'C'],
    'Category': ['X', 'X', 'Y', None, 'X', 'Y'],
    'Sales': [10, 20, 30, 40, None, 60]
}
df = pd.DataFrame(data)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Category</th>
      <th>Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>X</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>X</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>None</td>
      <td>Y</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>C</td>
      <td>None</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>B</td>
      <td>X</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>C</td>
      <td>Y</td>
      <td>60.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 6 entries, 0 to 5
    Data columns (total 3 columns):
     #   Column    Non-Null Count  Dtype  
    ---  ------    --------------  -----  
     0   City      5 non-null      object 
     1   Category  5 non-null      object 
     2   Sales     5 non-null      float64
    dtypes: float64(1), object(2)
    memory usage: 276.0+ bytes



```python
df['Category'].value_counts()
```




    Category
    X    3
    Y    2
    Name: count, dtype: int64




```python
df['Category'].value_counts(ascending=True, dropna=False)
```




    Category
    None    1
    Y       2
    X       3
    Name: count, dtype: int64




```python
df['City'].value_counts(normalize=True)
```




    City
    B    0.4
    C    0.4
    A    0.2
    Name: proportion, dtype: float64




```python
df['City'].value_counts()['C']
```




    np.int64(2)




```python
df['City'].unique()
```




    array(['A', 'B', None, 'C'], dtype=object)




```python
df.groupby('City')['Sales'].agg(['sum','min','max','mean', 'count'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sum</th>
      <th>min</th>
      <th>max</th>
      <th>mean</th>
      <th>count</th>
    </tr>
    <tr>
      <th>City</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>10.0</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>B</th>
      <td>20.0</td>
      <td>20.0</td>
      <td>20.0</td>
      <td>20.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>C</th>
      <td>100.0</td>
      <td>40.0</td>
      <td>60.0</td>
      <td>50.0</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



### Manipulating Data

#### 1. Adding Columns


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Category</th>
      <th>Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>X</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>X</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>None</td>
      <td>Y</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>C</td>
      <td>None</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>B</td>
      <td>X</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>C</td>
      <td>Y</td>
      <td>60.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
profit = [2,10,2,5,None,10]
df["Profit"] = profit
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>X</td>
      <td>10.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>None</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>C</td>
      <td>None</td>
      <td>40.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>B</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>C</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df["Ongoing"] = [True]*len(df)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>X</td>
      <td>10.0</td>
      <td>2.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>None</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>C</td>
      <td>None</td>
      <td>40.0</td>
      <td>5.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4</th>
      <td>B</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
    </tr>
    <tr>
      <th>5</th>
      <td>C</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.insert(1, "ID", [i for i in range(len(df))], False) #False- Don't allow Duplicates
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>0</td>
      <td>X</td>
      <td>10.0</td>
      <td>2.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>1</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>None</td>
      <td>2</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>C</td>
      <td>3</td>
      <td>None</td>
      <td>40.0</td>
      <td>5.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4</th>
      <td>B</td>
      <td>4</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
    </tr>
    <tr>
      <th>5</th>
      <td>C</td>
      <td>5</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = df.assign(Quantity=[100*(np.random.randint(1,20)) for i in range(len(df))])
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>0</td>
      <td>X</td>
      <td>10.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>600</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>1</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>700</td>
    </tr>
    <tr>
      <th>2</th>
      <td>None</td>
      <td>2</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>1700</td>
    </tr>
    <tr>
      <th>3</th>
      <td>C</td>
      <td>3</td>
      <td>None</td>
      <td>40.0</td>
      <td>5.0</td>
      <td>True</td>
      <td>900</td>
    </tr>
    <tr>
      <th>4</th>
      <td>B</td>
      <td>4</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>1100</td>
    </tr>
    <tr>
      <th>5</th>
      <td>C</td>
      <td>5</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>1100</td>
    </tr>
  </tbody>
</table>
</div>



#### 2. Removing Rows and Columns


```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>0</td>
      <td>X</td>
      <td>10.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>600</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>1</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>700</td>
    </tr>
    <tr>
      <th>2</th>
      <td>None</td>
      <td>2</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>1700</td>
    </tr>
    <tr>
      <th>3</th>
      <td>C</td>
      <td>3</td>
      <td>None</td>
      <td>40.0</td>
      <td>5.0</td>
      <td>True</td>
      <td>900</td>
    </tr>
    <tr>
      <th>4</th>
      <td>B</td>
      <td>4</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>1100</td>
    </tr>
    <tr>
      <th>5</th>
      <td>C</td>
      <td>5</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>1100</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = df2.drop('City',axis=1)
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>X</td>
      <td>10.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>600</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>700</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>1700</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>None</td>
      <td>40.0</td>
      <td>5.0</td>
      <td>True</td>
      <td>900</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>1100</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>1100</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = df2.loc[0:6:2,['ID','Category','Sales']]
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>X</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Y</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>X</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = df.assign(Quantity=[100*(np.random.randint(1,20)) for i in range(len(df))])
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>0</td>
      <td>X</td>
      <td>10.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>1600</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>1</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>400</td>
    </tr>
    <tr>
      <th>2</th>
      <td>None</td>
      <td>2</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>C</td>
      <td>3</td>
      <td>None</td>
      <td>40.0</td>
      <td>5.0</td>
      <td>True</td>
      <td>1800</td>
    </tr>
    <tr>
      <th>4</th>
      <td>B</td>
      <td>4</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>700</td>
    </tr>
    <tr>
      <th>5</th>
      <td>C</td>
      <td>5</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>500</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.drop('City', axis=1, inplace=True)
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>X</td>
      <td>10.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>1600</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>400</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>None</td>
      <td>40.0</td>
      <td>5.0</td>
      <td>True</td>
      <td>1800</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>700</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>500</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.drop(0,inplace=True)
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>400</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>None</td>
      <td>40.0</td>
      <td>5.0</td>
      <td>True</td>
      <td>1800</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>700</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>500</td>
    </tr>
  </tbody>
</table>
</div>



#### 3. Adding Rows


```python
newdf = pd.DataFrame({
    "ID":[6,7],
    "Category":['Y','X'],
    "Sales": [15, 5],
    "Profit": [20, 50],
    "Ongoing": [True, False],
    "Quantity": [200, 20]
})
df2 = pd.concat([df2, newdf],ignore_index=True)
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>400</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>600</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>None</td>
      <td>40.0</td>
      <td>5.0</td>
      <td>True</td>
      <td>1800</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>700</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Y</td>
      <td>15.0</td>
      <td>20.0</td>
      <td>True</td>
      <td>200</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>X</td>
      <td>5.0</td>
      <td>50.0</td>
      <td>False</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.loc[len(df2)] = [len(df2)+1,'Y',10,2,False,500]
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>400</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>600</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>None</td>
      <td>40.0</td>
      <td>5.0</td>
      <td>True</td>
      <td>1800</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>700</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Y</td>
      <td>15.0</td>
      <td>20.0</td>
      <td>True</td>
      <td>200</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>X</td>
      <td>5.0</td>
      <td>50.0</td>
      <td>False</td>
      <td>20</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Y</td>
      <td>10.0</td>
      <td>2.0</td>
      <td>False</td>
      <td>500</td>
    </tr>
  </tbody>
</table>
</div>



#### 4. Set Index


```python
df.drop(0,axis=0,inplace=True)
df.reset_index(inplace=True)
df.drop('index',axis=1,inplace=True)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>B</td>
      <td>1</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>None</td>
      <td>2</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>3</td>
      <td>None</td>
      <td>40.0</td>
      <td>5.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>B</td>
      <td>4</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4</th>
      <td>C</td>
      <td>5</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.set_index("ID", inplace=True)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
    </tr>
    <tr>
      <th>ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>None</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>C</td>
      <td>None</td>
      <td>40.0</td>
      <td>5.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4</th>
      <td>B</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
    </tr>
    <tr>
      <th>5</th>
      <td>C</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



### Conditional Selection


```python
 df2 == 10
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>5</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>6</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>7</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2[df2==10]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>10.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>10.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>10.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2[df2==10]['Profit']
```




    0    10.0
    1     NaN
    2     NaN
    3     NaN
    4    10.0
    5     NaN
    6     NaN
    7     NaN
    Name: Profit, dtype: float64




```python
df2[(df2['ID']%2==0) & (df2['Profit']!=10)]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>700</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Y</td>
      <td>15.0</td>
      <td>20.0</td>
      <td>True</td>
      <td>200</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Y</td>
      <td>10.0</td>
      <td>2.0</td>
      <td>False</td>
      <td>500</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2[(df2['ID']%2!=0) | (df2['Profit']==10)]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>400</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>None</td>
      <td>40.0</td>
      <td>5.0</td>
      <td>True</td>
      <td>1800</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>500</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>X</td>
      <td>5.0</td>
      <td>50.0</td>
      <td>False</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>



### Handling Missing Data


```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>400</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>600</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>None</td>
      <td>40.0</td>
      <td>5.0</td>
      <td>True</td>
      <td>1800</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>700</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Y</td>
      <td>15.0</td>
      <td>20.0</td>
      <td>True</td>
      <td>200</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>X</td>
      <td>5.0</td>
      <td>50.0</td>
      <td>False</td>
      <td>20</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Y</td>
      <td>10.0</td>
      <td>2.0</td>
      <td>False</td>
      <td>500</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.isnull()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>5</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>6</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>7</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2_nonullrow = df2.dropna(axis=0)
df2_nonullrow
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>400</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>600</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Y</td>
      <td>15.0</td>
      <td>20.0</td>
      <td>True</td>
      <td>200</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>X</td>
      <td>5.0</td>
      <td>50.0</td>
      <td>False</td>
      <td>20</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Y</td>
      <td>10.0</td>
      <td>2.0</td>
      <td>False</td>
      <td>500</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2_nonullcol = df2.dropna(axis=1)
df2_nonullcol
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>True</td>
      <td>400</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>True</td>
      <td>600</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>True</td>
      <td>1800</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>True</td>
      <td>700</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>True</td>
      <td>500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>True</td>
      <td>200</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>False</td>
      <td>20</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>False</td>
      <td>500</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>400</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>600</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>None</td>
      <td>40.0</td>
      <td>5.0</td>
      <td>True</td>
      <td>1800</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>700</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Y</td>
      <td>15.0</td>
      <td>20.0</td>
      <td>True</td>
      <td>200</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>X</td>
      <td>5.0</td>
      <td>50.0</td>
      <td>False</td>
      <td>20</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Y</td>
      <td>10.0</td>
      <td>2.0</td>
      <td>False</td>
      <td>500</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2_fillednull = df2.fillna('NA')
df2_fillednull
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>400</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>600</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>NA</td>
      <td>40.0</td>
      <td>5.0</td>
      <td>True</td>
      <td>1800</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>X</td>
      <td>NA</td>
      <td>NA</td>
      <td>True</td>
      <td>700</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Y</td>
      <td>15.0</td>
      <td>20.0</td>
      <td>True</td>
      <td>200</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>X</td>
      <td>5.0</td>
      <td>50.0</td>
      <td>False</td>
      <td>20</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Y</td>
      <td>10.0</td>
      <td>2.0</td>
      <td>False</td>
      <td>500</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2_fillednull.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 8 entries, 0 to 7
    Data columns (total 6 columns):
     #   Column    Non-Null Count  Dtype 
    ---  ------    --------------  ----- 
     0   ID        8 non-null      int64 
     1   Category  8 non-null      object
     2   Sales     8 non-null      object
     3   Profit    8 non-null      object
     4   Ongoing   8 non-null      bool  
     5   Quantity  8 non-null      int64 
    dtypes: bool(1), int64(2), object(3)
    memory usage: 392.0+ bytes


### Functions


```python
def tentimes(x):
    return x*10
```


```python
df2_nonullrow
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>400</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>600</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Y</td>
      <td>15.0</td>
      <td>20.0</td>
      <td>True</td>
      <td>200</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>X</td>
      <td>5.0</td>
      <td>50.0</td>
      <td>False</td>
      <td>20</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Y</td>
      <td>10.0</td>
      <td>2.0</td>
      <td>False</td>
      <td>500</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2_nonullrow['Quantity'].apply(tentimes)
```




    0    4000
    1    6000
    4    5000
    5    2000
    6     200
    7    5000
    Name: Quantity, dtype: int64




```python
df2_nonullrow['Profit'].apply(lambda x: x**2)
```




    0     100.0
    1       4.0
    4     100.0
    5     400.0
    6    2500.0
    7       4.0
    Name: Profit, dtype: float64




```python
df2_nonullrow[['Sales','Profit']].apply(tentimes)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Sales</th>
      <th>Profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>200.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>300.0</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>600.0</td>
      <td>100.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>150.0</td>
      <td>200.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>50.0</td>
      <td>500.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>100.0</td>
      <td>20.0</td>
    </tr>
  </tbody>
</table>
</div>



### Sorting and Ordering


```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>400</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>600</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>None</td>
      <td>40.0</td>
      <td>5.0</td>
      <td>True</td>
      <td>1800</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>700</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Y</td>
      <td>15.0</td>
      <td>20.0</td>
      <td>True</td>
      <td>200</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>X</td>
      <td>5.0</td>
      <td>50.0</td>
      <td>False</td>
      <td>20</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Y</td>
      <td>10.0</td>
      <td>2.0</td>
      <td>False</td>
      <td>500</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.sort_values('Sales', ascending=False, inplace=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>None</td>
      <td>40.0</td>
      <td>5.0</td>
      <td>True</td>
      <td>1800</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>600</td>
    </tr>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>400</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Y</td>
      <td>15.0</td>
      <td>20.0</td>
      <td>True</td>
      <td>200</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Y</td>
      <td>10.0</td>
      <td>2.0</td>
      <td>False</td>
      <td>500</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>X</td>
      <td>5.0</td>
      <td>50.0</td>
      <td>False</td>
      <td>20</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>700</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.sort_values('Category')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Category</th>
      <th>Sales</th>
      <th>Profit</th>
      <th>Ongoing</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>X</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>400</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>700</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>X</td>
      <td>5.0</td>
      <td>50.0</td>
      <td>False</td>
      <td>20</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Y</td>
      <td>30.0</td>
      <td>2.0</td>
      <td>True</td>
      <td>600</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Y</td>
      <td>60.0</td>
      <td>10.0</td>
      <td>True</td>
      <td>500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>Y</td>
      <td>15.0</td>
      <td>20.0</td>
      <td>True</td>
      <td>200</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Y</td>
      <td>10.0</td>
      <td>2.0</td>
      <td>False</td>
      <td>500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>None</td>
      <td>40.0</td>
      <td>5.0</td>
      <td>True</td>
      <td>1800</td>
    </tr>
  </tbody>
</table>
</div>


