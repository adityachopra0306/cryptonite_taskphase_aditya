# Logistic Regression

Logistic Regression is a Binary Classification Algorithm that is used when the target variable is categorical. It models the probability of a certain class (like 0 or 1) using a logistic(sigmoid) function.

The goal of logistic regression is to find the best-fitting model that predicts the probability of an instance belonging to a particular class. The model outputs values between 0 and 1, which are interpreted as probabilities.

## Theory

### Hypothesis function for Logistic Regression

The hypothesis function for logistic regression is expressed as:

$$
h_\theta(x) = g(\theta^Tx)
$$

where $g(z) = \frac{1}{1+e^{-z}}$ is the **Sigmoid Function**.  

Hence, we have:

$$
h_\theta(x) = \frac{1}{1 + e^{-\theta^T x}}
$$

where:
- $h_\theta(x)$ is the predicted probability that the instance belongs to class 1.
- $\theta$ is the parameter vector.
- $x$ is the feature vector.

### Log-Likelihood Function for Logistic Regression

To train the logistic regression model, we aim to maximise the log-likelihood function, which represents the success rate of the model:

$$
\ell(\theta) = \sum_{i=1}^{m} \ [ \ y^ilog(h_\theta(x^i)) + (1-y^i)log(1-h_\theta(x^i)) \ ]
$$

Where:
- $m$ is the number of training examples.
- $y^i$ is the label for the $i^{th}$ training example (either 0 or 1).
- $h_\theta(x^i)$ is the predicted probability for the $i^{th}$ training example.

### Gradient Ascent

To maximize the log-likelihood function and find the optimal values for the parameters $ \theta $, we use **Gradient Ascent**. The update rule for each parameter $ \theta_j $ is:

$$
    \theta_j := \theta_j + \sum_{i=1}^m \ \frac{\partial{\ell(\theta)}}{\partial{\theta_j}}
$$

By substituting the value of l(\theta) from above and solving the derivatives, we get:

$$
\theta_j := \theta_j + \alpha \sum_{i=1}^{m} \ (y^i - h_\theta(x^i)) x_j^i
$$

Where:
- $ \alpha $ is the learning rate.
- $ m $ is the number of training examples.

## Implementation

The implementation writeup can be found [here](LogisticRegression.md), and the Jupyter Notebook can be found [here](LogisticRegression.ipynb).