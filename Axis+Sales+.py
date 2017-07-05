
# coding: utf-8

# In[42]:

# Introduction
# Axis Auto Sales
# Carlos Hugens is the Sales Manager for Axis Auto Sales a low cost regional chain of Used Car Lots.
# Carlos is getting ready for his annual sales meeting and he is looking for the best way to improve his
# sales group's performance.
# His data includes the gender, years of experience, sales training and hours worked per week. It also
# includes the average cars sold per month by each salesperson.


# In[43]:

# Import Libraries
import pandas as pd
import numpy as np


# In[44]:

Location = "C:\\users\\Matthew\\Desktop\\Datasets\\axisdata.csv"


# In[45]:

df = pd.read_csv(Location)


# In[46]:

df.head()


# In[47]:

# To determine average cars sold:
df['Cars Sold'].mean()


# In[48]:

# To determine maximum number of cars sold:
df['Cars Sold'].max()


# In[49]:

# To determine minimum numbber of cars sold:
df['Cars Sold'].min()


# In[50]:

# To convert Gender value to numeric for easier analysis:
def score_to_numeric(x):
    if x=='F':
        return 1
    if x=='M':
        return 0


# In[51]:

# To apply numeric value to Gender:
df['gender_val'] = df['Gender'].apply(score_to_numeric) 


# In[52]:

df.tail()


# In[53]:

# To determine the average numbers of cars sold by men:
df.loc[df['gender_val']==0]['Cars Sold'].mean()


# In[54]:

# To determine the average number of cars sold by women:
df.loc[df['gender_val']==1]['Cars Sold'].mean()


# In[55]:

# To determine the average hours worked by those selling greater than 3 cars:
df.loc[df['Cars Sold']>3]['Hours Worked'].mean()


# In[56]:

# To determine the average years of experience:
df['Years Experience'].mean()


# In[57]:

# The average years of experience for those selling more than 3 cars:
df.loc[df['Cars Sold']>3]['Years Experience'].mean()


# In[58]:

# To convert Sales Training values to numeric values: 
def score_to_numeric(x):
    if x=='N':
        return 0
    if x=='Y':
        return 1


# In[59]:

# To apply numeric values to Sales Training:
df['Sales Training_val'] = df['SalesTraining'].apply(score_to_numeric)


# In[60]:

df.tail()


# In[61]:

# To calculate the average cars sold by those who did not receive sales training:
df.loc[df['Sales Training_val']==0]['Cars Sold'].mean()


# In[62]:

# To calculate the average cars sold by those who received sales training:
df.loc[df['Sales Training_val']==1]['Cars Sold'].mean()


# In[63]:


import statsmodels.formula.api as sm


# In[64]:

#To determine best indicators as to whether or not someone is a good salesperson
df.corr()
# A good sales person is defined by the number of cars sold
# Hours worked showed the strongest correlation with Cars Sold and hence the best indicator.


# In[65]:

# Conclusion
# Axis Auto Sales sold an average of four cars per months. Gender of sales person was in no way related to the # of cars sold
# Sales training and years of sales experience had little value. To increase his sales group performance Mr. Hugens should 
# focus on increasing the number of hours worked by each sales person as there is a 25% correlation. Mr. Hugens should 
# consider doing a feasibility study to determine what other factors he can employ to increase car sales.   


# In[ ]:



