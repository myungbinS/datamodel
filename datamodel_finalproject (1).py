#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[20]:


# A회사 보습제 화장품 매출 데이터 
df=pd.read_csv('C:/datamodel/MACOSX/A1data.csv', encoding='cp949')
print(df.to_string())


# In[39]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[63]:


plt.bar(df['날짜'],df['총매출'])
plt.xlabel('month')
plt.ylabel('total revenue')
plt.title('monthly total revenue')
plt.show()


# In[36]:


# 꺾은선 그래프 만들기
df['1온스별 단가'].plot()
plt.show()


# In[32]:


df['1온스별 단가']


# In[31]:


df.index=df['날짜']
df


# In[38]:


plt.scatter(df[''], df[''])


# In[65]:


plt.plot(df['날짜'],df['광고비용'], color='red')
plt.plot(df['날짜'],df['소셜네트워크 비용'], color='blue')
plt.xlabel('month')
plt.ylabel('cost')
plt.title('advertise cost and sns cost')
plt.show()


# In[62]:


plt.plot(df['날짜'],df['목표매출'], color='red')
plt.plot(df['날짜'],df['총매출'], color='green')
plt.xlabel('month')
plt.ylabel('revenue')
plt.title('goal revenu and total revenue')
plt.show()


# In[ ]:




