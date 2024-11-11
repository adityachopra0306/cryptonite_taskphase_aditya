# Linear Regression

Linear Regression is a Regression Algorithm, subclass of Supervised Learning Techniques, where the goal is to get a hypothesis function $h(x)$ corresponding to the given dataset of training examples such that $h(x)$ is a line which fits the datapoints.
New datapoints can then be found by finding the target variable corresponding to the given features in accordance with the hypothesis function. 


## Theory

### How to represent $h(x)$ ?

Let $m$ be the number of training examples in the dataset.
Let $x_j$ be a feature, $n$ be the number of features, and  $y$ the target variable for each training example in the dataset. 

Thus the $i^{th}$ training example can be represented as $(x^i,y^i), \quad 1<i<m$ where $m$ represents the total number of training examples.

Hence we get the hypothesis function $h$:

$$
h_\theta(x_1,x_2,\dots,x_n) = \theta_0 + \theta_1x_1 + \theta_2x_2 + \dots +  \theta_nx_n \\
 = \sum_{j=0}^n \theta_jx_j, \quad x_0=1
$$

Let $\theta$ be the parameter vector and $x$ be the feature vector as below:

$$
\theta = \begin{pmatrix}
\theta_0 \\
\theta_1 \\
\dots \\
\theta_n
\end{pmatrix}
,
\quad

x = \begin{pmatrix}
x_0 \\
x_1 \\
\dots \\
x_n
\end{pmatrix} \quad
where \ x_0 = 1
$$

Now it is clear that $h_\theta(x)$ can be represented by the equation:

$$
h_\theta(x)\ = \ \theta^Tx
$$

where $\theta_T$ is the transpose of the parameter vector.


### Goal

The goal in Linear Regression is to find the optimal value for the parameter vector $\theta$ such that: $$h_\theta(x^i)\approx y^i \ \forall \ 1<i<m$$

Formally, we define the parameter vector $\theta$ such that it minimises the **Mean Squared Error** cost function:

$$
    J(\theta)=\frac{1}{2} \ \sum_{i=1}^m \ (h_\theta(x^i)-y^i)^2
$$


### Batch Gradient Descent

1. Start with some value for each $\theta_j$ in parameter vector $\theta$. ( Say $\theta = \vec{0}$ )  
2. Then change $\theta$ repeatedly to reduce $J(\theta)$ as:
    $$
    \theta_j := \theta_j - \alpha(\frac{\partial J(\theta)}{\partial \theta_j})
    $$
    where $\alpha$ is the Learning Rate.  
3. Now repeat the same for all $\theta_j \in [0,n]$  
4. Repeat till $J(\theta)$ converges.


#### Note:

1. It can be derived that:

    $$
        \frac{\partial J(\theta)}{\partial \theta_j} = \sum_{i=1}^m \ (h_\theta(x^i)-y^i)x_j
    $$

    Thus the new Gradient Descent Function becomes:

    $$
    \theta_j := \theta_j - \alpha(\sum_{i=1}^m \ (h_\theta(x^i)-y^i)x_j)
    $$

2. The gradient descent method provides a local minima in terms of the value of the parametric vector. It can be observed that $J(\theta)$ is quadratic in x. Thus it will only have 1 local minima which will be the global minima. Hence gradient descent is guaranteed to work effectively.
3. The learning rate $\alpha$ influences the effectiveness of the algorithm. Too low of a learning rate makes the training very slow, while too high may cause overshot leading to the minima not being found.

### Stochastic Gradient Descent

The disadvantage of Batch Gradient Descent is that for each j, it sums up $(h_\theta(x^i)-y^i)x_j$ for all training examples. For a large dataset, this makes Batch Gradient Descent inefficient in time.  

Stochastic Gradient Descent uses a slightly different approach in order to achieve quicker training.

Here for each training example, all $\theta_j$ in the parameter vector $\theta$ is updated as:
    $$
        \theta_j := \theta_j - \alpha(h_\theta(x^i)-y^i)x_j^i
    $$

Hence the algorithm goes in the direction which minimises $h_\theta(x^i)-y^i$ for each individual training example, leading to $J(\theta)$ going in direction of minima *on average*. This makes Stochastic GD a more efficient but slightly less accurate training algorithm.


## Locally Weighted Regression

Locally Weighted Regression is a non-parametric algorithm (i.e. the number of parameters grows with the size of the dataset). In this algorithm, a weight is assigned to each training example. This weight depends upon the input for that particular test case.

Formally, we minimise the cost function:
    $$
        J(\theta) = \sum_{i=1}^m w^i(h_\theta(x^i)-y^i)^2
    $$
    Here,
    $$
        w^i = exp(\frac{-(x^i-x)^2}{2\tau^2})
    $$
    where $x^i$ is the $i^{th}$ training example, $x$ is the current input and $\tau$ is the bandwidth hyperparameter.

The bandwidth parameter $\tau$, also called the smoothing parameter decides the decay distance of the weights. A high value for $\tau$ smoothes the model, causing consideration of more data points around each test data point. This may lead to underfitting in extreme cases. A low value, on the other hand, captures local patterns as it only considers data points in close proximity to the query, risking overfitting in some cases.


## Implementation

The implementation writeup can be found [here](LinearRegression.md), and Jupyter Notebook can be found [here](LinearRegression.ipynb).