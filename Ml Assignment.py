#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[14]:


#Using NumPy create random vector of size 15 having only Integers in the range 1-20.
random_vector = np.random.randint(low=1, high=17, size=15)
arr_3x5 = random_vector.reshape(3, 5)
print(arr_3x5)
print(arr_3x5.shape)
arr_3x5[np.arange(3), arr_3x5.argmax(axis=1)] = 0
print(arr_3x5)


# In[9]:


import numpy as np
#program to compute the eigenvalues and right eigenvectors of a given square array given below:
A = np.array([[3, -2], [1, 0]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print("Right eigenvectors:\n", eigenvectors)


# In[6]:


#Compute the sum of the diagonal element of a given array.
A = np.array([[0, 1, 2], [3, 4, 5]])
sum = np.trace(A)
print("Sum of diagonal elements:", sum)


# In[10]:


#program to create a new shape to an array without changing its data. 
A = np.array([[1, 2], [3, 4], [5, 6]])
B = A.reshape((2, 3))
print("Original array:\n", A)
print("Reshaped array:\n", B)


# In[13]:


import matplotlib.pyplot as plt
#Python programming to create a below chart of the popularity of programming Languages.
languages = ['Java','Python','PHP','JavaScript','C','C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.pie(popularity, labels=languages, autopct='%1.1f%%')
plt.title('Popularity of Programming Languages')
plt.show()


# In[ ]:




