# NumPy

NumPy (Numerical Python) is a powerful library in Python for numerical and matrix computations, making it essential for data science, machine learning, and scientific computing. It provides support for large, multi-dimensional arrays and matrices, along with a large collection of mathematical functions and operations.

## Features

- **Efficient Array Computations**: Enables fast operations on arrays and matrices,
- **Broadcasting**: Allows operations on arrays of different shapes, and
- **Linear Algebra, Fourier Transform, and Random Number Generation**.

The NumPy library needs to be installed through pip, after which it can be imported into a python project


```python
import numpy as np
```

## Creating Arrays

### 1. From a Python list


```python
np.array([0,1,2,3,4,5,6,7,8,9])
```




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
npn = np.array([[1,2,3],[4,5,6],[7,8,9]])
```

 

### 2. Within a given range


```python
np.arange(1,10,2)
```




    array([1, 3, 5, 7, 9])



 

### 3. Zeros and Ones


```python
np.zeros(15)
np.ones(20)
```




    array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
           1., 1., 1.])




```python
np.zeros((3,3))
```




    array([[0., 0., 0.],
           [0., 0., 0.],
           [0., 0., 0.]])



### 3. Constant Value Array


```python
np.full((3,3),9)
```




    array([[9, 9, 9],
           [9, 9, 9],
           [9, 9, 9]])



### 4. Identity Matrix


```python
np.eye(3)
```




    array([[1., 0., 0.],
           [0., 1., 0.],
           [0., 0., 1.]])



### 5. Linspace


```python
np.linspace(0,1,5)
```




    array([0.  , 0.25, 0.5 , 0.75, 1.  ])



### 6. Random Integers


```python
np.random.randint(1,20,(3,3))
```




    array([[14, 17, 12],
           [ 3,  5,  3],
           [14,  3, 19]])



### 7. Uniform Distribution


```python
np.random.rand(2,3)
```




    array([[0.12488042, 0.82736202, 0.209198  ],
           [0.08980869, 0.68828787, 0.88105102]])



### 8. Normal Distribution


```python
np.random.randn(2,3)
```




    array([[-0.91370026,  0.10140186,  1.55363589],
           [ 0.27070123, -0.56710342,  1.03802025]])



### 9. Diagonal Matrix


```python
np.diag([1,2,3])
```




    array([[1, 0, 0],
           [0, 2, 0],
           [0, 0, 3]])



## Array Operations

### 1. Accessing Elements


```python
np1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])
print(np1[1,2])
```

    6


### 2. Slicing


```python
#Slice one-dimensional array
print(np1[2:9:2])
```

    [[7 8 9]]



```python
#Slicing multidimensional array
npn = np.arange(1,10,1).reshape(3,3)
print(npn[0:2, 1:3])
```

    [[2 3]
     [5 6]]


### 3. Mathematical operations


```python
#Square root each element
print(np.sqrt(np1))
```

    [[1.         1.41421356 1.73205081]
     [2.         2.23606798 2.44948974]
     [2.64575131 2.82842712 3.        ]]



```python
#Exponents
print(np.exp(np1))
```

    [[2.71828183e+00 7.38905610e+00 2.00855369e+01]
     [5.45981500e+01 1.48413159e+02 4.03428793e+02]
     [1.09663316e+03 2.98095799e+03 8.10308393e+03]]



```python
npr = np.random.randint(-10,11,(10,))
npr
```




    array([-10,   6,  -7,   8,  -3,  -3,   2,   1,  -6,   2])




```python
#Signum Function
print(np.sign(npr))
```

    [-1  1 -1  1 -1 -1  1  1 -1  1]



```python
#Trigonometry and Logarithms
print(np.sin(npr), end = '\n\n')
print(np.cos(npr), end = '\n\n')
print(np.tan(npr), end = '\n\n')
print(np.log(np1), end = '\n\n')
```

    [ 0.54402111 -0.2794155  -0.6569866   0.98935825 -0.14112001 -0.14112001
      0.90929743  0.84147098  0.2794155   0.90929743]
    
    [-0.83907153  0.96017029  0.75390225 -0.14550003 -0.9899925  -0.9899925
     -0.41614684  0.54030231  0.96017029 -0.41614684]
    
    [-0.64836083 -0.29100619 -0.87144798 -6.79971146  0.14254654  0.14254654
     -2.18503986  1.55740772  0.29100619 -2.18503986]
    
    [[0.         0.69314718 1.09861229]
     [1.38629436 1.60943791 1.79175947]
     [1.94591015 2.07944154 2.19722458]]
    



```python
#Add Subtract Multiply Divide element-wise
print((np1 + 10), end= "\n\n")  #Broadcasts [10] to shape (3,3)
print(np.subtract(np.array([[10,20,30],[40,50,60],[70,80,90]]),np1), end= "\n\n")
print((np1 * np.array([10])), end= "\n\n")
print(np.divide(np1,np.array([10])), end= "\n\n")
```

    [[11 12 13]
     [14 15 16]
     [17 18 19]]
    
    [[ 9 18 27]
     [36 45 54]
     [63 72 81]]
    
    [[10 20 30]
     [40 50 60]
     [70 80 90]]
    
    [[0.1 0.2 0.3]
     [0.4 0.5 0.6]
     [0.7 0.8 0.9]]
    


### 4. Statistical Operations


```python
npr = np.random.randint(-10,11,(10,))
npr
```




    array([  5,  -2,  -1,  -7,   2,   5,  -8,   7, -10,   3])




```python
#Min and Max
print(np.min(npr))
print(np.max(npr))
```

    -10
    7



```python
#Sum
print(np.sum(npr))
```

    -6



```python
#Mean, Median, Standard Deviation, Variance
print(np.mean(npr))
print(np.median(npr))
print(np.std(npr))
print(np.var(npr))
```

    -0.6
    0.5
    5.71314274283428
    32.64


### 5. Matrix Operations


```python
#Dot Product
a = np.arange(1,11)
b = np.arange(20,0,-2)
print(a)
print(b)
print(np.dot(a,b))
```

    [ 1  2  3  4  5  6  7  8  9 10]
    [20 18 16 14 12 10  8  6  4  2]
    440



```python
#Matrix Multiplication
a = a.reshape(2,5)
b = b.reshape(5,2)
print(a, end="\n\n")
print(b, end="\n\n")
print(a@b)
```

    [[ 1  2  3  4  5]
     [ 6  7  8  9 10]]
    
    [[20 18]
     [16 14]
     [12 10]
     [ 8  6]
     [ 4  2]]
    
    [[140 110]
     [440 360]]


### 6. Linear Algebra


```python
a = np.array([
    [1,2],
    [3,4]])
b = np.array([5,6])
```


```python
#Trace of Matrix
print(np.trace(a))
```

    5



```python
#Norm of Matrix
print(np.linalg.norm(a))
```

    5.477225575051661



```python
#Determinant of Matrix
print(np.linalg.det(a))
```

    -2.0000000000000004



```python
#Inverse of Matrix
print(np.linalg.inv(a))
```

    [[-2.   1. ]
     [ 1.5 -0.5]]



```python
#Solving System of Linear Equations
print(np.linalg.solve(a,b))
```

    [-4.   4.5]


### 7. Copying and Viewing


```python
#Default (Numpy view)
np2 = np1
np2[0] = 1000
print(np1)
```

    [[1000 1000 1000]
     [   4    5    6]
     [   7    8    9]]



```python
#View
np3 = np1.view()
np3[0]=0
print(np1)
```

    [[0 0 0]
     [4 5 6]
     [7 8 9]]



```python
#Copy
np2 = np1.copy()
np2[0]=1000
print(np1)
print(np2)
```

    [[0 0 0]
     [4 5 6]
     [7 8 9]]
    [[1000 1000 1000]
     [   4    5    6]
     [   7    8    9]]


## Array Manipulation


```python
#Reshape Array
npn = np.arange(10,20).reshape(2,5)
print(npn, end = "\n\n")

npn = npn.reshape(-1) #Flattens the array (ALTERNATIVE: npn.flatten())
print(npn)

npn = npn.reshape(2,5)
```

    [[10 11 12 13 14]
     [15 16 17 18 19]]
    
    [10 11 12 13 14 15 16 17 18 19]



```python
#Transposing Array
npn = npn.T
print(npn)
```

    [[10 15]
     [11 16]
     [12 17]
     [13 18]
     [14 19]]



```python
#Iterating through Array
for x in np.nditer(npn):
    print(x)
```

    10
    11
    12
    13
    14
    15
    16
    17
    18
    19



```python
#Sorting
print(npr)
print(np.sort(npr))
```

    [  5  -2  -1  -7   2   5  -8   7 -10   3]
    [-10  -8  -7  -2  -1   2   3   5   5   7]



```python
#Sorting multidimensional array (Sorts each row)
npr = np.random.randint(1,31,10)
npr = npr.reshape(2,5)
print(npr)
print(np.sort(npr))
```

    [[29 29 28 13 19]
     [20  7 12 18 26]]
    [[13 19 28 29 29]
     [ 7 12 18 20 26]]



```python
#Search for condition
x = np.where(npr >= 9)
print(x)
```

    (array([0, 0, 0, 0, 0, 1, 1, 1, 1]), array([0, 1, 2, 3, 4, 0, 2, 3, 4]))



```python
#Filtering Array using Bool Array/List
boolarr = np.array([
    [True, True, False, False, True],
    [False, True, False, True, True]])
print(npr[boolarr])
```

    [29 29 19  7 18 26]



```python
#Filtering using condition
filtered = npr % 2 != 0
print(filtered)
print(npr[filtered])
```

    [[ True  True False  True  True]
     [False  True False False False]]
    [29 29 13 19  7]

