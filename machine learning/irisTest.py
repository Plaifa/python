#!/usr/bin/env python
# coding: utf-8

# In[118]:


#test Iris Machine learning


# In[138]:


from IPython.display import Image #display image lib

from IPython.core.interactiveshell import InteractiveShell #for run all code line in 1 cell
InteractiveShell.ast_node_interactivity = "all"

import seaborn as sns #ML package 
import pandas as pd #package for manage data frame
import numpy as np

import matplotlib.pyplot as plt #visualization
get_ipython().run_line_magic('matplotlib', 'inline')

from sklearn.model_selection import train_test_split #split train and test data

#use SVC (support Vector Machine classifier)
from sklearn.svm import SVC

#model Evaluation
from sklearn.metrics import classification_report,confusion_matrix


# In[120]:


Image('https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg/330px-Kosaciec_szczecinkowaty_Iris_setosa.jpg')
print("1. Iris setosa")
Image('https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Iris_versicolor_3.jpg/330px-Iris_versicolor_3.jpg')
print("2. Iris versicolor")
Image('https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Iris_virginica.jpg/330px-Iris_virginica.jpg')
print("3. Iris virginica")


# In[121]:


iris = sns.load_dataset('iris') #load dataset name Iris by function sns 
sns.get_dataset_names()


# In[122]:


iris.head() #show top row 5 data of file
iris.tail() #show last top row 5 data of file


# In[123]:


iris.info()


# In[124]:


sns.pairplot(iris,hue='species') #x-y axis (name,color) -- visualize data


# In[125]:


setosa = iris[iris['species']=='setosa'] #plot graph of setosa to see means of length
sns.kdeplot(setosa['sepal_width'],setosa['sepal_length'],cmap="plasma",shade=True,shade_lowest=False)

virginica = iris[iris['species']=='virginica'] #plot graph of virginica to see means of length
sns.kdeplot(virginica['sepal_width'],virginica['sepal_length'],cmap="viridis",shade=True,shade_lowest=False)

versicolor = iris[iris['species']=='versicolor'] #plot graph of versicolor to see means of length
sns.kdeplot(versicolor['sepal_width'],versicolor['sepal_length'],cmap="cividis",shade=True,shade_lowest=False)


# In[126]:


#Model training

X = iris.drop('species',axis=1) #iris set but cut column species off


# In[127]:


X.head()


# In[128]:


Y = iris['species']


# In[129]:


Y.head()


# In[135]:


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3) #train70+test30


# In[132]:


svc_model = SVC()


# In[136]:


svc_model.fit(X_train,Y_train)


# In[139]:


#Model Evaslustion
prediction = svc_model.predict(X_test)


# In[141]:


print(confusion_matrix(Y_test,prediction))  # model use to predict


# In[142]:


print(classification_report(Y_test,prediction))


# In[143]:


iris


# In[144]:


4.7
3.2
1.3
0.2
setosa


# In[146]:


svc_model.predict([[4.7,3.2,1.3,0.2]]) #prediction from array


# In[147]:


svc_model.predict([[4,4,4,4]])


# In[ ]:





# In[ ]:





# In[ ]:




