import numpy as np
import pandas as pd

class Node:
    def __init__(self, feature_index=None, threshold=None, left=None, right=None, label=None):
        self.j = feature_index
        self.t = threshold
        self.l = left
        self.r = right
        self.label = label

class DecisionTree:
    def __init__(self, max_depth = 5):
        self.max_d = max_depth

    def gini(self, y):
        classes, counts = np.unique(y, return_counts=True)
        p = counts/len(y)
        return 1-np.sum(p**2)

    def split(self,X,j,t):
        l_mask = X[:,j] <= t
        return l_mask, ~l_mask
    
    def best_split(self,X,y):
        best_j, best_t = None, None
        min_gini = float('inf')
        
        for j in range(X.shape[1]):
            possible_t = X[:,j]
            
            for t in possible_t:
                lm,rm = self.split(X,j,t)
                l, r = y[lm],y[rm]
                if len(l)==0 or len(r)==0:
                    continue
                
                g = (len(l)*self.gini(l) + len(r)*self.gini(r))/len(y)
                
                if g < min_gini:
                    min_gini =g
                    best_j = j
                    best_t = t
        return best_j, best_t

    def make_tree(self,X,y, curr_d=0):
        if len(np.unique(y)) == 1 or curr_d >= self.max_d or len(y) < 5:
            majority_class = np.bincount(y).argmax()
            return Node(label=majority_class)
            
        j,t = self.best_split(X,y)
        
        if j==None:
            majority_class = np.bincount(y).argmax()
            return Node(label=majority_class)
        
        lm,rm = self.split(X,j,t)
        l = self.make_tree(X[lm],y[lm],curr_d+1)
        r = self.make_tree(X[rm],y[rm],curr_d+1)
        return Node(j,t,l,r)

    def train(self, X, y):
        self.root = self.make_tree(X,y)
    
    def predict_single(self, x, node):
        if node.label is not None:
            return node.label
        if x[node.j] <= node.t:
            return self.predict_single(x,node.l)
        else:
            return self.predict_single(x,node.r)

    def predict(self, X_test):
        return np.array([self.predict_single(x, self.root) for x in X_test])
